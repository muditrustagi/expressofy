from rest_framework.response import Response
import traceback

"""
def get_request_url_from_request(request):
	print(request.get_full_path())
	return request.get_full_path()
"""

def get_data_dictionary_from_request(request):
	return request.data

def create_model_object_from_data_dictionary(data_dictionary,type_of_serializer,request):
	return type_of_serializer(data=data_dictionary, many=isinstance(data_dictionary, list))

def save_model_object_into_database_table(model_object):
	if model_object.is_valid():
		model_object.save()
		return Response(model_object.data)
	else:
		return Response(model_object.errors)

def get_model_object_using_pk(pk,database_table):
	return database_table.objects.filter(pk__in=pk)
	

def create_serialized_model_object_from_model_object(model_object,type_of_serializer):
	return type_of_serializer(model_object,many=True)

	
def update_model_object_using_data_dictionary(data_dictionary_list,model_object_list,type_of_serializer):
	for model_object in model_object_list.all():		
		for data_dictionary in data_dictionary_list:
			if data_dictionary[model_object._meta.pk.name]==model_object.pk:
				model_x=type_of_serializer(model_object,data=data_dictionary,partial=True)
				if model_x.is_valid():
					model_x.save()
		
	return model_object_list
	
def get_primary_key_list_from_data_dictionary(data_dictionary,key):
	return [element[key] for element in data_dictionary if key in element]


def data_controller(request,control_word,database_table,type_of_serializer,primary_key):
	switcher = {
				'CREATE'	:	create_data,
				'READ'		:	read_data,
				'UPDATE'	:	update_data,
				'DELETE'	:	delete_data
			}
	return switcher.get(control_word, error)(request,control_word,database_table,type_of_serializer,primary_key)


def create_data(request,control_word,database_table,type_of_serializer,primary_key):
	try:
		data_dictionary			=	get_data_dictionary_from_request(request)
		model_object			=	create_model_object_from_data_dictionary(data_dictionary,type_of_serializer,request)
		print(model_object)
		return						save_model_object_into_database_table(model_object)
	except:
		traceback.print_exc()
		return Response({"Error":"Could not be added"})


def read_data(request,control_word,database_table,type_of_serializer,primary_key):
	try:
		data_dictionary			=	get_data_dictionary_from_request(request)
		primary_key_list		=	get_primary_key_list_from_data_dictionary(data_dictionary,primary_key)
		model_object			=	get_model_object_using_pk(primary_key_list,database_table)
	
		if model_object:
			serialized_model_object	=	create_serialized_model_object_from_model_object(model_object,type_of_serializer)
			return Response(serialized_model_object.data)	
		else:
			traceback.print_exc()
			return Response({"Error":"Does not exist"})
	except:
		traceback.print_exc()
		return Response({"Error":"Could not be read"})


def update_data(request,control_word,database_table,type_of_serializer,primary_key):
	try:
		data_dictionary			=	get_data_dictionary_from_request(request)
		primary_key_list		=	get_primary_key_list_from_data_dictionary(data_dictionary,primary_key)
		model_object			=	get_model_object_using_pk(primary_key_list,database_table)
		updated_model_object	=	update_model_object_using_data_dictionary(data_dictionary,model_object,type_of_serializer)
		serialized_model_object	=	create_serialized_model_object_from_model_object(updated_model_object,type_of_serializer)
		return Response(serialized_model_object.data)
	except:
		traceback.print_exc()
		return Response({"Error":"Could not be updated"})


def delete_data(request,control_word,database_table,type_of_serializer,primary_key):
	try:
		data_dictionary			=	get_data_dictionary_from_request(request)
		primary_key_list		=	get_primary_key_list_from_data_dictionary(data_dictionary,primary_key)
		model_object			=	get_model_object_using_pk(primary_key_list,database_table)
		model_object.delete()
		return Response({"Success":"Deleted Successfully"})
	except:
		traceback.print_exc()
		return Response({"Error":"Could not be deleted"})


def error(request):
	return Response({"Error":"Control word not matched"})
