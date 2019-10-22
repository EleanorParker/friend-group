"""An example of how to represent a group of acquaintances in Python."""

my_group ={
	'Jill':{
		'Age':26
		'Job':'Biologist'
		'Relation to others':{
			'Jill':['self'],
			'Zalika':['friend'],
			'John':['partner'],
			'Nash':[],
		}
	}

	'Zalika':{
		'Age':28
		'Job':'Artist'
		'Relation to others':{
			'Jill':['friend'],
			'Zalika':['self'],
			'John':[],
			'Nash':['tenant'],
		}
	}

	'John':{
		'Age':27
		'Job':'Writer'
		'Relation to others':{  
			'Jill':['partner'],
                        'Zalika':[],
                        'John':['self'],
                        'Nash':['cousin'],
		}
	}

	'Nash':{
		'Age':34
		'Job':'Writer'
		'Relation to others':{
			'Jill':[],
			'Zalika':['landlord'],
			'John':['cousin']
			'Nash':['self']
		}
	}
}
