// Copyright © DarkSide Assasins. All rights reserved.
import 'dart:convert';

List<User> userFromJson(String str) =>
    List<User>.from(json.decode(str).map((x) => User.fromJson(x)));
String userToJson(List<User> data) =>
    json.encode(List<dynamic>.from(data.map((x) => x.toJson())));

class User {
  User({
    required this.id,
    required this.email,
    required this.password,
    required this.name,
    required this.phone,
    required this.role,
    required this.status,
  });
  int id;
  String email;
  String password;
  String name;
  String phone;
  bool role;
  String status;
  late String token;

  factory User.fromJson(Map<String, dynamic> json) => User(
      id: json["id"],
      email: json["email"],
      password: json["password"],
      name: json["name"],
      phone: json["phone"],
      role: json["role"],
      status: json["resp"]);

  Map<String, dynamic> toJson() => {
        "id": id,
        "name": name,
        "email": email,
        "password": password,
        "role": role,
        "phone": phone
      };
  Map<String, dynamic> retResp() => {"status": status};
}
