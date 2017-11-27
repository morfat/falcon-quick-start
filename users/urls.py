from .views import List,Detail,Authenticate


patterns=(('/users',List()),
          ('/users/{user_id}',Detail()),
         ('/users/authenticate',Authenticate()),

         )
