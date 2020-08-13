# Overview

Sample contains code to test the basic use case of dry-rest-permissions

# What `dry-rest-permissions` offers:

1. A framework for defining global and object level permissions per action.
2. Support for broadly defining permissions by grouping actions into safe and unsafe types.
3. Support for defining only global (table level) permissions or only object (row level) permissions.
4. Support for custom list and detail actions.
5. A serializer field that will return permissions for an object to your client app. This is DRY and works with your existing permission definitions.
6. A framework for limiting list requests based on permissions
