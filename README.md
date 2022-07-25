# Prerequisites

1. create `.env` at root level
2. add DB_URL with complete conn str; use `postgresql://` not `postgres://`

# Mac start env
1. from terminal window, run `source bin/activate`

# Mac stop env
1. from terminal window, run `deactivate`

# Generate DB tables
1. from terminal window, enter python shell with `python`
2. import db file with `from app import db`
2. run `db.create_all()`
4. check PG instance for table

# Add data to table manually
1. inside Python shell `from app import db`, `from api.models import Post`
2. `db.session.add(new_model_instance)`
3. `db.session.commit()`


# Postman
1. set to POST and body to GraphQL

```
query AllPosts {
  listPosts {
    success
    errors
    posts {
      id
      title 
      description
      created_at
    }
  }
}

query getPost {
    getPost(id: "1") {
    post {
      id
      title
      description
    }
    success
    errors
  }
}

mutation CreateNewPost {
  createPost(
    title: "New Blog Post", 
    description:"Some Description") {
    post {
      id
      title
      description
      created_at
    }
    success
    errors
  }
}

mutation UpdatePost {
  updatePost(id:"2", title:"Hello title", description:"updated description") {
    post {
      id
      title
      description
    }
    success
    errors
  }
}

mutation DeletePost {
  deletePost(id:"2") {
    post {
      id
      title
      description
    }
    success
    errors
  }
}

