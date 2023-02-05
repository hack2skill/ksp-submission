const router = require('express').Router();
const Stepone = require("./controllers/Stepone")

router.post('/apilink', Stepone.search)
router.post('/apilink/store', Stepone.store)
router.post('/apilink/que', Stepone.que)

module.exports = router;