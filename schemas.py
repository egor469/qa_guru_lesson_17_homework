get_single_user = {
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "data": {
      "type": "object",
      "properties": {
        "id": {
          "type": "integer"
        },
        "email": {
          "type": "string"
        },
        "first_name": {
          "type": "string"
        },
        "last_name": {
          "type": "string"
        },
        "avatar": {
          "type": "string"
        }
      },
      "required": [
        "id",
        "email",
        "first_name",
        "last_name",
        "avatar"
      ]
    },
    "support": {
      "type": "object",
      "properties": {
        "url": {
          "type": "string"
        },
        "text": {
          "type": "string"
        }
      },
      "required": [
        "url",
        "text"
      ]
    }
  },
  "required": [
    "data",
    "support"
  ]
}

post_great_new_user = {
    "$schema": "https://json-schema.org/draft/2019-09/schema",
    "$id": "http://example.com/example.json",
    "type": "object",
    "default": {},
    "title": "Root Schema",
    "required": [
        "name",
        "job",
        "id",
        "createdAt"
    ],
    "properties": {
        "name": {
            "type": "string",
            "default": "",
            "title": "The name Schema",
            "examples": [
                "morpheus"
            ]
        },
        "job": {
            "type": "string",
            "default": "",
            "title": "The job Schema",
            "examples": [
                "leader"
            ]
        },
        "id": {
            "type": "string",
            "default": "",
            "title": "The id Schema",
            "examples": [
                "958"
            ]
        },
        "createdAt": {
            "type": "string",
            "default": "",
            "title": "The createdAt Schema",
            "examples": [
                "2025-04-27T15:48:25.340Z"
            ]
        }
    },
    "examples": [{
        "name": "morpheus",
        "job": "leader",
        "id": "958",
        "createdAt": "2025-04-27T15:48:25.340Z"
    }]
}

put_update_user = {
    "$schema": "https://json-schema.org/draft/2019-09/schema",
    "$id": "http://example.com/example.json",
    "type": "object",
    "default": {},
    "title": "Root Schema",
    "required": [
        "name",
        "job",
        "updatedAt"
    ],
    "properties": {
        "name": {
            "type": "string",
            "default": "",
            "title": "The name Schema",
            "examples": [
                "morpheus"
            ]
        },
        "job": {
            "type": "string",
            "default": "",
            "title": "The job Schema",
            "examples": [
                "zion resident"
            ]
        },
        "updatedAt": {
            "type": "string",
            "default": "",
            "title": "The updatedAt Schema",
            "examples": [
                "2025-04-27T16:11:20.252Z"
            ]
        }
    },
    "examples": [{
        "name": "morpheus",
        "job": "zion resident",
        "updatedAt": "2025-04-27T16:11:20.252Z"
    }]
}

post_register_user = {
    "$schema": "https://json-schema.org/draft/2019-09/schema",
    "$id": "http://example.com/example.json",
    "type": "object",
    "default": {},
    "title": "Root Schema",
    "required": [
        "id",
        "token"
    ],
    "properties": {
        "id": {
            "type": "integer",
            "default": 0,
            "title": "The id Schema",
            "examples": [
                4
            ]
        },
        "token": {
            "type": "string",
            "default": "",
            "title": "The token Schema",
            "examples": [
                "QpwL5tke4Pnpja7X4"
            ]
        }
    },
    "examples": [{
        "id": 4,
        "token": "QpwL5tke4Pnpja7X4"
    }]
}


post_login_user = {
    "$schema": "https://json-schema.org/draft/2019-09/schema",
    "$id": "http://example.com/example.json",
    "type": "object",
    "default": {},
    "title": "Root Schema",
    "required": [
        "token"
    ],
    "properties": {
        "token": {
            "type": "string",
            "default": "",
            "title": "The token Schema",
            "examples": [
                "QpwL5tke4Pnpja7X4"
            ]
        }
    },
    "examples": [{
        "token": "QpwL5tke4Pnpja7X4"
    }]
}