class DepthSerializerMixin(object):
	"""Custom method 'get_serializer_class', set attribute 'depth' based on query parameter in the url"""
	
	def get_serializer_class(self):
		serializer_class = self.serializer_class
		query_params = self.request.QUERY_PARAMS
		depth = query_params.get('__depth', None)
		serializer_class.Meta.depth = int(depth) if(depth != None and depth.isdigit()) else 0
		return serializer_class
