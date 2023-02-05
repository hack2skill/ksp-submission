// Copyright © DarkSide Assasins. All rights reserved.
import 'package:flutter/material.dart';
import '../colors.dart';

import 'login_page.dart';

class HomePage extends StatefulWidget {
  const HomePage({super.key});

  @override
  State<HomePage> createState() => _HomePageState();
}

class _HomePageState extends State<HomePage> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: primary,
      body: getBody(context),
    );
  }
}

Widget getBody(BuildContext context) {
  return Scaffold(
      body: SingleChildScrollView(
    child: Center(
        child: Column(
      crossAxisAlignment: CrossAxisAlignment.center,
      mainAxisAlignment: MainAxisAlignment.spaceAround,
      children: [
        const SizedBox(
          height: 30,
        ),
        Image.network(
          'https://upload.wikimedia.org/wikipedia/commons/thumb/a/aa/Seal_of_Karnataka.svg/1200px-Seal_of_Karnataka.svg.png',
          height: 500,
          width: 800,
        ),
        const SizedBox(
          height: 30,
        ),
        const Text(
          'Welcome',
          style: TextStyle(fontWeight: FontWeight.bold, fontSize: 25),
        ),
        Expanded(
          flex: 0,
          child: Text(
            'Login to your account',
            style: TextStyle(
                color: Colors.white.withOpacity(0.5),
                fontWeight: FontWeight.w300,
                fontSize: 15),
          ),
        ),
        const SizedBox(
          height: 30,
        ),
        ElevatedButton(
            style: ElevatedButton.styleFrom(
                shape: RoundedRectangleBorder(
                    borderRadius: BorderRadius.circular(10.0)),
                backgroundColor: Colors.purple,
                padding: EdgeInsets.symmetric(
                    horizontal: MediaQuery.of(context).size.width / 3.3,
                    vertical: 20)),
            onPressed: () async {
              Navigator.push(context,
                  MaterialPageRoute(builder: (context) => const LoginPage()));
            },
            child: const Text(
              'Sounds Good!',
              style: TextStyle(fontSize: 17),
            )),
        const SizedBox(
          height: 30,
        ),
      ],
    )),
  ));
}
