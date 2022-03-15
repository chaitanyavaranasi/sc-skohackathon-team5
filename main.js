const { MongoClient, ObjectID } = require("mongodb");
const Express = require("express");
const Cors = require("cors");
const BodyParser = require("body-parser");
const { request } = require("express");

// const client = new MongoClient(process.env["ATLAS_URI"]);
const client = new MongoClient("mongodb+srv://demo_user:x4kiX5FoDfUBgdeA@znaydit.padcu.mongodb.net/myFirstDatabase?retryWrites=true&w=majority");
const server = Express();

server.use(BodyParser.json());
server.use(BodyParser.urlencoded({ extended: true }));
server.use(Cors());

var collection;
var port = process.env.PORT || 4000;

server.get("/search", async (request, response) => {
    try {
        let result = await collection.aggregate([
            {
                "$search": {
                    "autocomplete": {
                        "query": `${request.query.query}`,
                        "path": "name",
                        "fuzzy": {
                            "maxEdits": 2,
                            "prefixLength": 3
                        }
                    }
                }
            }
        ]).toArray();
        response.send(result);
    } catch (e) {
        response.status(500).send({ message: e.message });
    }
});

server.get("/get/:id", async (request, response) => {
    try {
        let result = await collection.findOne({ "_id": ObjectID(request.params.id) });
        response.send(result);
    } catch (e) {
        response.status(500).send({ message: e.message });
    }
});

server.listen(port, async () => {
    try {
        await client.connect();
        // collection = client.db("zynadit").collection("items");
        collection = client.db("food").collection("recipes");
    } catch (e) {
        console.error(e);
    }
console.log('Magic happens on port: ' + port);
});
