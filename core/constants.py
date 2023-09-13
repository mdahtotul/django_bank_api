def get_all_domains(domain_name):
    all_domains = [
        {
            "name": "home",
            "endpoint": domain_name,
            "token": "",
            "req_type": "GET",
            "access_role": "Public"

        },
        {
            "name": "auth-users",
            "endpoint": f"{domain_name}/auth/users",
            "token": "",
            "req_type": "GET, POST",
            "access_role": "Admin, Public"
        },
        {
            "name": "create JWT token",
            "endpoint": f"{domain_name}/auth/jwt/create",
            "token": "",
            "req_type": "POST",
            "access_role": "Public"
        },
        {
            "name": "refresh JWT token",
            "endpoint": f"{domain_name}/auth/jwt/refresh",
            "token": "",
            "req_type": "POST",
            "access_role": "Authenticated"
        },
        {
            "name": "bank",
            "endpoint": f"{domain_name}/bank/",
            "token": "",
            "req_type": "POST",
            "access_role": "Authenticated"
        },
        {
            "name": "branches",
            "endpoint": f"{domain_name}/bank/branches/",
            "token": "",
            "req_type": "POST",
            "access_role": "Authenticated"
        },
        {
            "name": "addresses",
            "endpoint": f"{domain_name}/bank/addresses/",
            "token": "",
            "req_type": "POST",
            "access_role": "Authenticated"
        },
        
    ]

    return all_domains