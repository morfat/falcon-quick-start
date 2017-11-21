from .views import List,Detail


patterns=(('/users',List()),
          ('/users/{user_id}',Detail()),
         )
