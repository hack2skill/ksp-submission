import 'dart:convert';
import 'dart:io';
import 'package:flutter/material.dart';
import 'package:frontend/dashboards/get_results.dart';
import 'package:frontend/services/user_api.dart';
import 'package:frontend/views/signup_page.dart';
import 'package:image_picker/image_picker.dart';
import 'package:path/path.dart';
import 'package:path_provider/path_provider.dart';

import '../views/home_page.dart';

class AdminDash extends StatefulWidget {
  const AdminDash({Key? key}) : super(key: key);

  @override
  State<AdminDash> createState() => _AdminDashState();
}

enum from_where { Police_db, social_media, both }

enum search_against { Image, Video, Both, Snap }

class _AdminDashState extends State<AdminDash> {
  XFile? image;
  late String finalPath;
  late List<int> img_bytes;
  final ImagePicker picker = ImagePicker();

  Future getImage(ImageSource media) async {
    var img = await picker.pickImage(source: media);
    setState(() {
      image = img;
    });
    if (img != null) {
      print("Image picked");
      print(image!.name);
      // image = img;
      img_bytes = await image!.readAsBytes();
    }
  }

  void myAlert(BuildContext context) {
    showDialog(
        context: context,
        builder: (BuildContext context) {
          return AlertDialog(
            shape:
                RoundedRectangleBorder(borderRadius: BorderRadius.circular(8)),
            title: Text('Please choose media to select'),
            content: Container(
              height: MediaQuery.of(context).size.height / 6,
              child: Column(
                children: [
                  ElevatedButton(
                    //if user click this button, user can upload image from gallery
                    onPressed: () {
                      Navigator.pop(context);
                      getImage(ImageSource.gallery);
                    },
                    child: Row(
                      children: [
                        Icon(Icons.image),
                        Text('From Gallery'),
                      ],
                    ),
                  ),
                ],
              ),
            ),
          );
        });
  }

  from_where? _choice = from_where.Police_db;

  // bool _value = false;
  search_against? _option = search_against.Both;
  bool viz = false;
  String resp = "Report";

  @override
  Widget build(BuildContext context) {
    String resprt;

    String val = _option.toString();
    return Scaffold(
      appBar: AppBar(
        elevation: 0,
        backgroundColor: const Color.fromRGBO(49, 87, 110, 1.0),
        title: Text('User Dashboard'),
        leading: IconButton(
            onPressed: () {
              Navigator.push(
                  context,
                  MaterialPageRoute(
                      builder: (BuildContext context) => const HomePage()));
            },
            icon: const Icon(
              Icons.home,
              size: 20,
              color: Colors.grey,
            )),
      ),
      body: SafeArea(
        child: Container(
          padding: EdgeInsets.symmetric(vertical: 20.0, horizontal: 2.0),
          child: SingleChildScrollView(
            //crossAxisCount: 2,
            padding: EdgeInsets.all(3.0),
            child: Center(
              child: Column(
                children: [
                  Card(
                      elevation: 1.0,
                      margin: EdgeInsets.all(50.0),
                      child: Container(
                        decoration: BoxDecoration(
                            color: Color.fromRGBO(220, 220, 220, 1.0)),
                        child: Builder(builder: (context) {
                          return InkWell(
                            onTap: () {
                              myAlert(context);
                            },
                            child: Center(
                              child: Column(
                                crossAxisAlignment: CrossAxisAlignment.stretch,
                                mainAxisSize: MainAxisSize.min,
                                verticalDirection: VerticalDirection.down,
                                children: const <Widget>[
                                  SizedBox(height: 50.0),
                                  Center(
                                      child: Icon(
                                    Icons.image,
                                    size: 60.0,
                                    color: Colors.black,
                                  )),
                                  SizedBox(height: 10.0),
                                  Padding(
                                    padding: EdgeInsets.all(8.0),
                                    child: Center(
                                      child: Text('Upload Image',
                                          style: TextStyle(
                                              fontSize: 20.0,
                                              color: Colors.black)),
                                    ),
                                  )
                                ],
                              ),
                            ),
                          );
                        }),
                      )),
                  image != null
                      ? Padding(
                          padding: const EdgeInsets.symmetric(horizontal: 40),
                          child: ClipRRect(
                            borderRadius: BorderRadius.circular(8),
                            child: Image.network(
                              //to show image, you type like this.
                              image!.path,
                              fit: BoxFit.cover,
                              //width: 200,
                              height: 400,
                            ),
                          ),
                        )
                      : Text('No image'),
                  SizedBox(
                    height: 10.0,
                  ),
                  Padding(
                    padding: const EdgeInsets.all(8),
                    child: Column(
                      children: [
                        SizedBox(
                          height: 60,
                        ),
                        const Text(
                          "From where",
                          textAlign: TextAlign.left,
                          style: TextStyle(
                              fontSize: 15,
                              fontWeight: FontWeight.w400,
                              color: Color.fromARGB(221, 248, 106, 106)),
                        ),
                        Divider(),
                        ListTile(
                          title: const Text('Police Database'),
                          leading: Radio<from_where>(
                            value: from_where.Police_db,
                            groupValue: _choice,
                            onChanged: (from_where? value) {
                              setState(() {
                                _choice = value;
                                // _value = true;
                              });
                            },
                          ),
                        ),
                        ListTile(
                          title: const Text('Social Media Platform'),
                          leading: Radio<from_where>(
                            value: from_where.social_media,
                            groupValue: _choice,
                            onChanged: (from_where? value) {
                              setState(() {
                                _choice = value;
                                // _value = true;
                              });
                            },
                          ),
                        ),
                        ListTile(
                          title: const Text('Both'),
                          leading: Radio<from_where>(
                            value: from_where.both,
                            groupValue: _choice,
                            onChanged: (from_where? value) {
                              setState(() {
                                _choice = value;
                                // _value = true;
                              });
                            },
                          ),
                        ),
                        const Text(
                          "Search Against",
                          textAlign: TextAlign.left,
                          style: TextStyle(
                              fontSize: 15,
                              fontWeight: FontWeight.w400,
                              color: Color.fromARGB(221, 248, 106, 106)),
                        ),
                        Divider(),
                        ListTile(
                          title: const Text('Image'),
                          leading: Radio<search_against>(
                            value: search_against.Image,
                            groupValue: _option,
                            onChanged: (search_against? value) {
                              setState(() {
                                _option = value;
                                val = value.toString();
                              });
                            },
                          ),
                        ),
                        ListTile(
                          title: const Text('Video'),
                          leading: Radio<search_against>(
                            value: search_against.Video,
                            groupValue: _option,
                            onChanged: (search_against? value) {
                              setState(() {
                                _option = value;
                                val = value.toString();
                                // _value = true;
                              });
                            },
                          ),
                        ),
                        ListTile(
                          title: const Text('Both'),
                          leading: Radio<search_against>(
                            value: search_against.Both,
                            groupValue: _option,
                            onChanged: (search_against? value) {
                              setState(() {
                                _option = value;
                                val = value.toString();
                                // _value = true;
                              });
                            },
                          ),
                        ),
                        ListTile(
                          title: const Text('Compare Images'),
                          leading: Radio<search_against>(
                            value: search_against.Snap,
                            groupValue: _option,
                            onChanged: (search_against? value) {
                              setState(() {
                                _option = value;
                                // _value = true;
                              });
                            },
                          ),
                        ),
                        Column(
                          children: [
                            Padding(
                              padding: const EdgeInsets.all(8.0),
                              child: MaterialButton(
                                minWidth: double.infinity,
                                height: 60,
                                onPressed: () async {
                                  String base64image = base64Encode(img_bytes);
                                  resprt = await UserApi().getResults(
                                      base64image, val, image!.name);
                                  setState(() {
                                    viz = true;
                                    resp = resprt;
                                  });
                                },
                                color: const Color.fromARGB(255, 252, 88, 88),
                                shape: RoundedRectangleBorder(
                                    borderRadius: BorderRadius.circular(40)),
                                child: const Text(
                                  "Get Result",
                                  style: TextStyle(
                                    fontWeight: FontWeight.w600,
                                    fontSize: 16,
                                  ),
                                ),
                              ),
                            ),
                            Visibility(
                                visible: viz,
                                child: Container(
                                    padding: const EdgeInsets.all(50),
                                    child: Text(resp))),
                          ],
                        ),
                      ],
                    ),
                  ),
                  Container(
                    padding: EdgeInsets.all(8.0),
                    child: Wrap(
                      alignment: WrapAlignment.spaceAround,
                      children: <Widget>[
                        Card(
                          child: Container(
                            width: 180,
                            height: 100,
                            child: Center(
                              child: Column(
                                children: [
                                  SizedBox(
                                    height: 23,
                                  ),
                                  Icon(Icons.person_add),
                                  SizedBox(
                                    height: 8.0,
                                  ),
                                  Text('Add User')
                                ],
                              ),
                            ),
                          ),
                        ),
                        SizedBox(
                          width: 20.0,
                        ),
                        Card(
                          child: Container(
                            width: 180,
                            height: 100,
                            child: Center(
                              child: Column(
                                children: [
                                  SizedBox(
                                    height: 23,
                                  ),
                                  Icon(Icons.delete),
                                  SizedBox(
                                    height: 8.0,
                                  ),
                                  Text('Remove Admin')
                                ],
                              ),
                            ),
                          ),
                        ),
                        SizedBox(
                          width: 20.0,
                        ),
                        Card(
                          child: Container(
                            width: 180,
                            height: 100,
                            child: Center(
                              child: Column(
                                children: [
                                  SizedBox(
                                    height: 23,
                                  ),
                                  Icon(Icons.edit),
                                  SizedBox(
                                    height: 8.0,
                                  ),
                                  Text('Modify Admin Details')
                                ],
                              ),
                            ),
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

  getResult(Map searchResults) {}
}
