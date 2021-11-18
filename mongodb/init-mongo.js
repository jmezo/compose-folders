db.createUser({
  user: "yourusername",
  pwd: "yourpwd",
  roles: [
    {
      role: "readWrite",
      db: "yourdb",
    },
  ],
});
