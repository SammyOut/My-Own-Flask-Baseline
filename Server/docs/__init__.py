def parameter(name: str, description: str, in_: str='json', type_: str='str', required: bool=True) -> dict:
    return {
        'name': name,
        'description': description,
        'in': in_,
        'type': type_,
        'required': required
    }


jwt_header = parameter('Authorization', 'JWT Token', 'header')
