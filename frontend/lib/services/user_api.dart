// Copyright © DarkSide Assasins. All rights reserved.
import 'dart:convert';
import 'package:http/http.dart' as http;
import '../models/user.dart';

class UserApi {
  Future<bool> startApp() async {
    bool start = false;
    var client = http.Client();
    var uri = Uri.parse("http://127.0.0.1:5000/");
    final http.Response response = await client.get(
      uri,
      headers: <String, String>{
        'Content-Type': 'application/json; charset=UTF-8',
      },
    );
    if (response.statusCode == 200) {
      start = true;
      print(response.body);
    }
    return start;
  }

  Future<int> addNewUser(String name, String email, bool role) async {
    int res = 0;
    var client = http.Client();
    var uri = Uri.parse("http://127.0.0.1:5000/admin/addNewUser");
    final http.Response response = await client.post(
      uri,
      headers: <String, String>{
        'Content-Type': 'application/json; charset=UTF-8',
      },
      body: jsonEncode(
          <String, dynamic>{'name': name, 'email': email, 'role': role}),
    );
    print(response.body);
    if (response.statusCode == 200) {
      if (response.body.contains("added")) {
        res = 1;
      } else if (response.body.contains("already")) {
        res = 2;
      } else if (response.body.contains("confirm")) {
        res = 3;
      }
    } else {
      print("Something went wrong");
      throw Exception("Failed to load server");
    }
    return res;
  }

  Future<User> loginUser(String email, String password) async {
    var client = http.Client();
    var uri = Uri.parse("http://127.0.0.1:5000/login");
    final http.Response response = await client.post(
      uri,
      headers: <String, String>{
        'Content-Type': 'application/json; charset=UTF-8',
      },
      body: jsonEncode(<String, dynamic>{'email': email, 'password': password}),
    );
    if (response.statusCode == 200) {
      User instance;
      if (response.body.contains("resp") == true) {
        instance = User.fromJson(jsonDecode(response.body));
      } else {
        String msg;
        msg = (response.body.contains("Password"))
            ? "Password Incorrect"
            : "Username doesn't exist, please contact the admin";
        instance = User(
            id: -1,
            email: "",
            password: "",
            name: "",
            phone: "",
            role: false,
            status: msg);
      }
      return instance;
    } else {
      throw Exception('Failed to Save User.');
    }
  }

  Future<String> getResults(String image, String search, String name) async {
    String res = " ";
    var client = http.Client();
    var uri = Uri.parse("http://127.0.0.1:5000/admin/search");
    final http.Response response = await client.post(uri,
        headers: <String, String>{
          'Content-Type': 'application/json; charset=UTF-8',
        },
        body: jsonEncode(
            {"img_path": image, "search_against": search, "name": name}));

    if (response.statusCode == 200) {
      res = jsonDecode(response.body)["Report"];
      print(res);
    }
    return res;
  }

  Future<Map> displayResults() async {
    Map res = Map();
    var client = http.Client();
    var uri = Uri.parse("http://127.0.0.1:5000/admin/search");
    final http.Response response =
        await client.get(uri, headers: <String, String>{
      'Content-Type': 'application/json; charset=UTF-8',
    });

    if (response.statusCode == 200) {
      res = jsonDecode(response.body);
      print("got it");
    }
    print(res);
    return res;
  }
}
