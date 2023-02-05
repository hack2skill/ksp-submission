// Copyright © DarkSide Assasins. All rights reserved.
import 'dart:convert';

import 'package:flutter/material.dart';
import 'package:frontend/services/user_api.dart';

class GetResults extends StatefulWidget {
  const GetResults({Key? key}) : super(key: key);

  @override
  State<GetResults> createState() => _GetResultsState();
}

class _GetResultsState extends State<GetResults> {
  bool viz = false;
  String report = '';
  @override
  void initState() {
    report = "Output";
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
        appBar: AppBar(
          title: Text("Here for results"),
        ),
        body: SingleChildScrollView(
          child: Center(
              child: Column(
            children: [
              MaterialButton(
                minWidth: 80,
                height: 60,
                child: Text("Generate"),
                onPressed: () async {
                  var resp = await UserApi().displayResults();
                  setState(() {
                    viz = true;
                    report = resp['Report'];
                  });
                },
              ),
              Visibility(
                  visible: viz,
                  child: Container(
                      padding: const EdgeInsets.all(50), child: Text(report))),
            ],
          )),
        ));
  }
}
