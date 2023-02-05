// Copyright © DarkSide Assasins. All rights reserved.
import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';
import 'package:lottie/lottie.dart';

import '../dashboards/admin_dashboard.dart';
import '../dashboards/user_dashboard.dart';
import '../services/user_api.dart';

class LoginPage extends StatefulWidget {
  const LoginPage({Key? key}) : super(key: key);

  @override
  State<LoginPage> createState() => _LoginPageState();
}

class _LoginPageState extends State<LoginPage> {
  final _userEmail = TextEditingController();
  final _passWord = TextEditingController();
  bool _validateEmail = false;
  bool _validatePass = false;
  final bool _correctPass = true;

  @override
  void dispose() {
    _userEmail.clear();
    _passWord.clear();
    super.dispose();
  }

  bool isEmailCorrect = false;
  final _formKey = GlobalKey<FormState>();

  @override
  Widget build(BuildContext context) {
    void showSnacBar(BuildContext context, String msg) {
      final snacBar = SnackBar(
          behavior: SnackBarBehavior.floating,
          content: Padding(
            padding: const EdgeInsets.symmetric(horizontal: 10),
            child: Container(
              padding: const EdgeInsets.symmetric(horizontal: 40),
              height: 35,
              child: Center(
                child: Text(
                  msg,
                  style: const TextStyle(
                    color: Colors.black,
                    fontWeight: FontWeight.bold,
                    fontSize: 20,
                  ),
                ),
              ),
            ),
          ));
      ScaffoldMessenger.of(context).showSnackBar(snacBar);
    }

    return Scaffold(
      appBar: AppBar(
        elevation: 0,
        backgroundColor: Colors.transparent,
        leading: IconButton(
            onPressed: () {
              Navigator.push(
                  context,
                  MaterialPageRoute(
                      builder: (BuildContext context) => const LoginPage()));
            },
            icon: const Icon(
              Icons.home,
              size: 20,
              color: Colors.grey,
            )),
      ),
      body: Container(
        decoration: const BoxDecoration(
            image: DecorationImage(
                image: NetworkImage(
                    'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSx7IBkCtYd6ulSfLfDL-aSF3rv6UfmWYxbSE823q36sPiQNVFFLatTFdGeUSnmJ4tUzlo&usqp=CAU'),
                fit: BoxFit.cover,
                opacity: 0.3)),
        child: SafeArea(
          child: Center(
            child: SingleChildScrollView(
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.center,
                mainAxisAlignment: MainAxisAlignment.center,
                children: [
                  Lottie.network(
                      'https://assets6.lottiefiles.com/packages/lf20_k9wsvzgd.json',
                      animate: true,
                      height: 120,
                      width: 600),
                  Text(
                    'Log In Now',
                    style: GoogleFonts.indieFlower(
                      textStyle: const TextStyle(
                        fontWeight: FontWeight.bold,
                        fontSize: 40,
                      ),
                    ),
                  ),
                  Text(
                    'Please login to continue using our app',
                    style: GoogleFonts.indieFlower(
                      textStyle: TextStyle(
                          color: Colors.black.withOpacity(0.5),
                          fontWeight: FontWeight.w500,
                          fontSize: 15),
                    ),
                  ),
                  const SizedBox(
                    height: 30,
                  ),
                  Padding(
                    padding: const EdgeInsets.symmetric(horizontal: 40),
                    child: Column(
                      children: [
                        Form(
                          key: _formKey,
                          child: Column(
                            children: [
                              TextFormField(
                                  controller: _userEmail,
                                  validator: (currentValue) {
                                    var nonNullValue = currentValue ?? '';
                                    if (nonNullValue.isEmpty) {
                                      return ("Email is required");
                                    }
                                    if (!nonNullValue.contains("@")) {
                                      return ("Invalid email");
                                    }
                                    return null;
                                  },
                                  style: const TextStyle(
                                      fontSize: 15,
                                      fontWeight: FontWeight.w400,
                                      color:
                                          Color.fromARGB(221, 248, 106, 106)),
                                  decoration: const InputDecoration(
                                    border: OutlineInputBorder(),
                                    hintText: 'Enter Email',
                                    labelText: 'Email',
                                  )),
                              const SizedBox(
                                height: 20.0,
                              ),
                              TextFormField(
                                  controller: _passWord,
                                  obscureText: true,
                                  validator: (passCurrentValue) {
                                    var passNonNullValue =
                                        passCurrentValue ?? "";
                                    if (passNonNullValue.isEmpty) {
                                      return ("Password is required");
                                    } else if (passNonNullValue.length < 6) {
                                      return ("Password Must be more than 5 characters");
                                    } else if (_correctPass == false) {
                                      return ("Incorrect Password entered");
                                    }
                                    return null;
                                  },
                                  decoration: const InputDecoration(
                                    border: OutlineInputBorder(),
                                    hintText: 'Enter Password',
                                    labelText: 'Password',
                                  )),
                              const SizedBox(
                                height: 20.0,
                              ),
                              MaterialButton(
                                minWidth: double.infinity,
                                height: 60,
                                onPressed: () async {
                                  if (_formKey.currentState!.validate()) {
                                    if (_validateEmail == false &&
                                        _validatePass == false) {
                                      var res = await UserApi().loginUser(
                                          _userEmail.text, _passWord.text);
                                      if (res.id != -1) {
                                        if (res.role == true) {
                                          // ignore: use_build_context_synchronously
                                          Navigator.push(
                                              context,
                                              MaterialPageRoute(
                                                  builder:
                                                      (BuildContext context) =>
                                                          const AdminDash()));
                                        } else {
                                          // ignore: use_build_context_synchronously
                                          Navigator.push(
                                              context,
                                              MaterialPageRoute(
                                                  builder:
                                                      (BuildContext context) =>
                                                          const UserDash()));
                                        }
                                      } else {
                                        showSnacBar(context, res.status);
                                      }
                                    }
                                  }
                                },
                                color: const Color.fromARGB(255, 252, 88, 88),
                                shape: RoundedRectangleBorder(
                                    borderRadius: BorderRadius.circular(40)),
                                child: const Text(
                                  "Login",
                                  style: TextStyle(
                                    fontWeight: FontWeight.w600,
                                    fontSize: 16,
                                  ),
                                ),
                              ),
                            ],
                          ),
                        ),
                      ],
                    ),
                  ),
                ],
              ),
            ),
          ),
        ),
      ),
    );
  }
}
