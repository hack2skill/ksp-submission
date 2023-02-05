// Copyright © DarkSide Assasins. All rights reserved.
import 'package:flutter/material.dart';
import 'package:frontend/services/user_api.dart';
import 'package:google_fonts/google_fonts.dart';

import 'colors.dart';
import 'views/home_page.dart';

void main() async {
  bool start = false;
  start = await UserApi().startApp();
  if (start)
    runApp(const MyApp());
  else
    print("Something went wrong");
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      
      debugShowCheckedModeBanner: false,
      title: 'Karnatak State Police',
      theme: ThemeData.dark().copyWith(
        scaffoldBackgroundColor: bgColor,
        textTheme: GoogleFonts.poppinsTextTheme(
            Theme.of(context).textTheme.apply(bodyColor: Colors.white)),
        canvasColor: secondaryColor,
      ),
      home: const HomePage(),
    );
  }
}
