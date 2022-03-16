const express = require('express')
const axios = require('axios')
const app = express()
const port = 3000
console.log("starting");

// app.get('/', (req, res) => {
//   res.send('Hello World!')
// })

app.listen(port, () => {
  console.log(`Example app listening on port ${port}`)
})

app.use(express.static(`${__dirname}/public`));

app.get('/findOne', (req, res) => {
  var data = JSON.stringify({
    "collection": "items",
    "database": "zynadit",
    "dataSource": "Znaydit",
    // "projection": {
    //     "_id": 1
    // }
  });
  var config = {
    method: 'post',
    url: 'https://data.mongodb-api.com/app/data-zbccb/endpoint/data/beta/action/findOne',
    headers: {
        'Content-Type': 'application/json',
        'Access-Control-Request-Headers': '*',
        'api-key': 'SxHIn5sT899cpLqZtEvQedn1sPe7buxFNPvvjR8K7dEvmpntk5ocvbJcpjvwsuWC'
    },
    data : data
  };

  axios(config)
    .then(function (response) {
//        console.log(JSON.stringify(response.data));
        res.send(JSON.stringify(response.data));
    })
    .catch(function (error) {
        console.log(error);
    });
})

console.log("ending");
