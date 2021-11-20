db.createUser({
  user: "readUser",
  pwd: "password",
  roles: [{ role: "read", db: "default" }],
});
db.createUser({
  user: "readWriteUser",
  pwd: "password",
  roles: [{ role: "dbAdmin", db: "default" }],
});
