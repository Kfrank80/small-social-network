## Social Network

[[_TOC_]]

---

:scroll: **START**


### Introduction

Social networks have transformed the way we communicate, advertise and lead our lives during the past 2 decades.
Many of us have one or multiple profiles on one or several networks, and we use them on a daily basis to communicate and share information.

---

### Task description

We are tasked with developing a small social network, where **users** can _create_ their profiles, make _friends_ or _follow_ each other.
They are able to create **posts**, which could be _public_ (visible to their friends and followers), or _private_ (only visible to their friends).

The users that can see a post, have also the option to _like_ (or _unlike_ if they've liked it before).
A single user can only like a single post once (they can like as many posts as they like, but each individual only once).

Finally, all users can request to see their wall, which is a list of all the posts created by themselves, their friends, and the public posts of the people they follow.

The **user** has:
- fullName: the user's full name

The **posts** have:
- text: A string value, representing the contents of the post
- visibility: can be either **public** or **private**

Develop a set of REST service APIs based on the swagger file provided - [swagger file](social-network-swagger.yaml), that allows users to:
- Users can create their profiles (`POST /users`)
- They can make friends or follow other users (`POST /users/{user1Id}/{friends|followers}/{user2Id}`)
- For the follower relationship, the second passed userId becomes a follower of the first passed userId (user1Id <-isFollowedBy- user2Id)
- They can create posts, that are public or private (`POST /posts`)
- Request to see their wall, which contains all posts that are visible to them, sorted by latest to earliest (from the creation time descending) (`GET /walls/{userId}`)

You can open the swagger file using a tool like [Swagger Editor](https://editor.swagger.io/), which provides a good visual representation of the methods needed, their format, sample requests and responses.

### Requirements

While implementing your solution **please take care of the following requirements**:

#### Functional requirements

- The REST API methods should be implemented based on the specification provided in the linked swagger file;
- Add 2 new API methods (they're not defined in the swagger file) that enable a user to like a post, and unlike a post they've already liked. When returning the list of posts in the `/walls` method, add a new attribute to each post returned, containing the number of likes it has;
- There is no need for UI.

#### Non-functional requirements

- The project must be buildable and runnable;
- The project must have Unit tests;
- The project must have a README file with build/run/test instructions (use a DB that can be run locally, e.g. in-memory, via container);
- Any data required by the application to run (e.g. reference tables, dummy data) must be preloaded in the database;
- Input/output data must be in JSON format;
- Use a framework of your choice, but popular, up-to-date, and long-term support versions are recommended.

---
:scroll: **END**
