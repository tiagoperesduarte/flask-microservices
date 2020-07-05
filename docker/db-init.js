db.createUser(
    {
        user: "root",
        pwd: "myroot",
        roles:[
            {
                role: "readWrite",
                db:   "flask-microservices"
            }
        ]
    }
);