// Copyright © DarkSide Assasins. All rights reserved.
import 'package:flutter/material.dart';
import 'package:frontend/dashboards/admin_dashboard.dart';
import 'package:frontend/views/login_page.dart';
import '../services/user_api.dart';

class SignupPage extends StatefulWidget {
  const SignupPage({Key? key}) : super(key: key);

  @override
  State<SignupPage> createState() => _SignupPageState();
}

enum Roles { user, admin }

class _SignupPageState extends State<SignupPage> {
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

  final _userEmail = TextEditingController();
  final _name = TextEditingController();
  final _formKey = GlobalKey<FormState>();
  Roles? _character = Roles.user;
  bool _value = false;

  @override
  Widget build(BuildContext context) {
    return Scaffold(
        backgroundColor: const Color.fromARGB(255, 55, 18, 50),
        body: SafeArea(
            child: SingleChildScrollView(
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.center,
            mainAxisAlignment: MainAxisAlignment.spaceEvenly,
            children: [
              Column(
                mainAxisAlignment: MainAxisAlignment.spaceEvenly,
                children: [
                  const SizedBox(
                    height: 30,
                  ),
                  Image.network(
                    'https://upload.wikimedia.org/wikipedia/commons/thumb/a/aa/Seal_of_Karnataka.svg/1200px-Seal_of_Karnataka.svg.png',
                    height: 300,
                    width: 600,
                  ),
                  const SizedBox(
                    height: 30,
                  ),
                  const Text(
                    "Add new user as Admin or User",
                    style: TextStyle(
                        fontSize: 30,
                        fontWeight: FontWeight.bold,
                        color: Color.fromARGB(221, 128, 17, 128)),
                  ),
                  const SizedBox(
                    height: 20,
                  ),
                  Text(
                    "Add an user",
                    style: TextStyle(
                      fontSize: 15,
                      color: Colors.grey[700],
                    ),
                  ),
                  const SizedBox(
                    height: 30,
                  )
                ],
              ),
              Padding(
                padding: const EdgeInsets.symmetric(horizontal: 40),
                child: Form(
                  key: _formKey,
                  child: Column(
                    children: [
                      TextFormField(
                          controller: _name,
                          validator: (currentValue) {
                            var nonNullValue = currentValue ?? '';
                            if (nonNullValue.isEmpty) {
                              return ("Name is required");
                            }
                          },
                          style: const TextStyle(
                              fontSize: 15,
                              fontWeight: FontWeight.w400,
                              color: Color.fromARGB(221, 248, 106, 106)),
                          decoration: const InputDecoration(
                            border: OutlineInputBorder(),
                            hintText: 'Enter Name',
                            labelText: 'Name',
                          )),
                      const SizedBox(
                        height: 20.0,
                      ),
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
                              color: Color.fromARGB(221, 248, 106, 106)),
                          decoration: const InputDecoration(
                            border: OutlineInputBorder(),
                            hintText: 'Enter Email',
                            labelText: 'Email',
                          )),
                      const SizedBox(
                        height: 20.0,
                      ),
                      Column(
                        children: [
                          const Align(
                            alignment: Alignment.centerLeft,
                            child: Text(
                              "Assign Role",
                              textAlign: TextAlign.left,
                              style: TextStyle(
                                  fontSize: 15,
                                  fontWeight: FontWeight.w400,
                                  color: Color.fromARGB(221, 248, 106, 106)),
                            ),
                          ),
                          const Divider(),
                          ListTile(
                            title: const Text('Admin'),
                            leading: Radio<Roles>(
                              value: Roles.admin,
                              groupValue: _character,
                              onChanged: (Roles? value) {
                                setState(() {
                                  _character = value;
                                  _value = true;
                                });
                              },
                            ),
                          ),
                          ListTile(
                            title: const Text('User'),
                            leading: Radio<Roles>(
                              value: Roles.user,
                              groupValue: _character,
                              onChanged: (Roles? value) {
                                setState(() {
                                  _character = value;
                                  _value = false;
                                });
                              },
                            ),
                          ),
                        ],
                      ),
                      const SizedBox(
                        height: 20.0,
                      ),
                      MaterialButton(
                        minWidth: double.infinity,
                        height: 60,
                        onPressed: () async {
                          if (_formKey.currentState!.validate()) {
                            var res = await UserApi().addNewUser(
                                _name.text, _userEmail.text, _value);

                            // ignore: use_build_context_synchronously
                            showSnacBar(context, "Processing");

                            if (res != 0) {
                              String msg;
                              if (res == 1) {
                                msg =
                                    "User added successfully, check inbox to confirm url, then login";
                              } else if (res == 2) {
                                msg = "User already exists, login";
                              } else {
                                msg =
                                    "User has to confirm from email, check inbox";
                              }
                              // ignore: use_build_context_synchronously
                              showDialog(
                                  context: context,
                                  builder: (_) => AlertDialog(
                                        title: const Text("Alert"),
                                        content: Text(msg),
                                        actions: <Widget>[
                                          TextButton(
                                              onPressed: () => {
                                                    Navigator.push(
                                                        context,
                                                        MaterialPageRoute(
                                                            builder: (BuildContext
                                                                    context) =>
                                                                const LoginPage())),
                                                  },
                                              child: const Text("OK"))
                                        ],
                                      ));
                            } else {
                              String msg = "Something went wrong";
                              Future.delayed(Duration.zero)
                                  .then((value) => AlertDialog(
                                        title: const Text("Alert"),
                                        content: Text(msg),
                                        actions: <Widget>[
                                          TextButton(
                                              onPressed: () => {
                                                    Navigator.push(
                                                        context,
                                                        MaterialPageRoute(
                                                            builder: (BuildContext
                                                                    context) =>
                                                                const AdminDash())),
                                                  },
                                              child: const Text("OK"))
                                        ],
                                      ));
                            }
                          }
                        },
                        color: const Color.fromARGB(255, 252, 88, 88),
                        shape: RoundedRectangleBorder(
                            borderRadius: BorderRadius.circular(40)),
                        child: const Text(
                          "Add",
                          style: TextStyle(
                            fontWeight: FontWeight.w600,
                            fontSize: 16,
                          ),
                        ),
                      ),
                      const SizedBox(
                        height: 20,
                      ),
                    ],
                  ),
                ),
              )
            ],
          ),
        )));
  }
}
