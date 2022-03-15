const express = require('express')
const axios = require('axios')
const app = express()
const port = 3000

app.get('/', (req, res) => {
  res.send('Hello World!')
})
https://runkit.com/
app.listen(port, () => {
  console.log(`Example app listening on port ${port}`)
})

app.get('/findOne', (req, res) => {
  console.log(data)
  var axios = require('axios');
  var data = JSON.stringify({
    "collection": "items",
    "database": "zynadit",
    "dataSource": "Znaydit",
    "projection": {
        "_id": 1
    }
  });
  var config = {
    method: 'post',
    url: 'https://data.mongodb-api.com/app/data-zbccb/endpoint/data/beta/action/findOne',
    headers: {
        'Content-Type': 'application/json',
        'Access-Control-Request-Headers': '*',
        'api-key': '<API_KEY>'
    },
    data : data
  };

  axios(config)
    .then(function (response) {
        console.log(JSON.stringify(response.data));
    })
    .catch(function (error) {
        console.log(error);
    });
})
