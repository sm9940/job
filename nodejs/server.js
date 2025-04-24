const express = require('express')
const app = express()
// const cors = require('cors')
// app.use(cors())
app.get('/', function (req, res) {
   return res.send('안녕하세요')
})
app.listen(3000, function () {
   console.log('server listening on port 3000')
})
