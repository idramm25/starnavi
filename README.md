How to:

   URL: 
	localhost:8000/api/articles/

   Create Post:
	curl -X POST -d "title=Hello world 3&description=HWDescription&body=HWBody&author_id=<author_id>" URL

--------------------------------------------------------------------------

   Get List of Posts:
        curl localhost:8000/api/articles/

--------------------------------------------------------------------------

   Get Post:
	curl localhost:8000/api/articles/<post_id>/

--------------------------------------------------------------------------

   Modify Post:
	curl -X PUT -d "author_id=1&title=NEW&description=NEW&body=NEW" URL

--------------------------------------------------------------------------

   Delete Post:
	curl -X DELETE localhost:8000/api/articles/<post_id>/

