using UnityEngine;
using System.Collections;
using UnityEngine.UI;
using System.IO;
using System.Collections.Generic;

public class CSVParsing : MonoBehaviour
{
    public string csvFile; // Reference of CSV file
    //public InputField rollNoInputField;// Reference of rollno input field
    //public InputField nameInputField; // Reference of name input filed
    //public Text contentArea; // Reference of contentArea where records are displayed

    private char lineSeperater = '\n'; // It defines line seperate character
    private char fieldSeperator = ','; // It defines field seperate chracter

    private string Log_Type = "CSVParsing";

    private string[] allRecordData;

    void Start()
    {
        var path = Path.Combine(Application.streamingAssetsPath, "Sample Missing Persons FIRS.csv");

        csvFile = File.ReadAllText(path);

        Debug.Log(Log_Type + " Start " + File.ReadAllText(path));

        readData();
    }
    // Read data from CSV file
    private void readData()
    {
        string[] records = csvFile.Split(lineSeperater);

        allRecordData = records;

        foreach (string record in records)
        {

            Debug.Log(Log_Type + " Start ");

            Debug.Log(Log_Type + " Data " + record);

            Debug.Log(Log_Type + " End ");

            string[] fields = record.Split(fieldSeperator);
            foreach (string field in fields)
            {
                //contentArea.text += field + "\t";
            }
            //contentArea.text += '\n';
        }
    }

    public string[] ReturnAdditionInfo(string photoID)
    {
        var data = new List<string>();

        foreach (string record in allRecordData)
        {
            if(record.Contains(photoID))
            {
                string[] fields = record.Split(fieldSeperator);

                data.Add(fields[16]);

                data.Add(fields[17]);

                data.Add(fields[10]);
            }
        }

        return data.ToArray();

    }

    // Add data to CSV file
//    public void addData()
//    {
//        // Following line adds data to CSV file
//        File.AppendAllText(getPath() + "/Assets/StudentData.csv", lineSeperater + rollNoInputField.text + fieldSeperator + nameInputField.text);
//        // Following lines refresh the edotor and print data
//        rollNoInputField.text = "";
//        nameInputField.text = "";
//        contentArea.text = "";
//#if UNITY_EDITOR
//        UnityEditor.AssetDatabase.Refresh();
//#endif
//        readData();
//    }

    // Get path for given CSV file
    private static string getPath()
    {
        #if UNITY_EDITOR
                return Application.dataPath;
        #elif UNITY_ANDROID
        return Application.persistentDataPath;// +fileName;
        #elif UNITY_IPHONE
        return GetiPhoneDocumentsPath();// +"/"+fileName;
        #else
        return Application.streamingAssetsPath;// +"/"+ fileName;
        #endif
    }
    // Get the path in iOS device
    private static string GetiPhoneDocumentsPath()
    {
        string path = Application.dataPath.Substring(0, Application.dataPath.Length - 5);
        path = path.Substring(0, path.LastIndexOf('/'));
        return path + "/Documents";
    }

}