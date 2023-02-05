const arr = [
    {
      "label": "identity_attack",
      "results": [
        {
          "probabilities": {
            "0": 0.9324270486831665,
            "1": 0.06757296621799469
          },
          "match": false
        },
        {
          "probabilities": {
            "0": 0.9709845185279846,
            "1": 0.02901551127433777
          },
          "match": false
        }
      ]
    },
    {
      "label": "insult",
      "results": [
        {
          "probabilities": {
            "0": 0.8709426522254944,
            "1": 0.12905734777450562
          },
          "match": null
        },
        {
          "probabilities": {
            "0": 0.9155324101448059,
            "1": 0.08446762710809708
          },
          "match": false
        }
      ]
    },
    {
      "label": "obscene",
      "results": [
        {
          "probabilities": {
            "0": 0.9445523619651794,
            "1": 0.055447619408369064
          },
          "match": false
        },
        {
          "probabilities": {
            "0": 0.972429096698761,
            "1": 0.027570929378271103
          },
          "match": false
        }
      ]
    },
    {
      "label": "severe_toxicity",
      "results": [
        {
          "probabilities": {
            "0": 0.9984152317047119,
            "1": 0.0015847235918045044
          },
          "match": false
        },
        {
          "probabilities": {
            "0": 0.9993953704833984,
            "1": 0.0006046105409041047
          },
          "match": false
        }
      ]
    },
    {
      "label": "sexual_explicit",
      "results": [
        {
          "probabilities": {
            "0": 0.8979986906051636,
            "1": 0.10200132429599762
          },
          "match": null
        },
        {
          "probabilities": {
            "0": 0.9382796883583069,
            "1": 0.06172029674053192
          },
          "match": false
        }
      ]
    },
    {
      "label": "threat",
      "results": [
        {
          "probabilities": {
            "0": 0.2782358229160309,
            "1": 0.7217641472816467
          },
          "match": null
        },
        {
          "probabilities": {
            "0": 0.3562313914299011,
            "1": 0.6437686085700989
          },
          "match": null
        }
      ]
    },
    {
      "label": "toxicity",
      "results": [
        {
          "probabilities": {
            "0": 0.1648763120174408,
            "1": 0.8351237177848816
          },
          "match": null
        },
        {
          "probabilities": {
            "0": 0.26768818497657776,
            "1": 0.7323118448257446
          },
          "match": null
        }
      ]
    }
  ]

  let obj = {};
  arr.forEach((e) =>{
    let s = 0;
    e.results.forEach((e) =>{
        s+=e.probabilities['1'];
    })

    let name = e.label;
    obj[name] = s/2;
    s = 0;

  })

  console.log(obj)