using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using System.Net;
using UnityEngine.Networking;
using System.IO;
using TMPro;
using Gravitons.UI.Modal;
using System;
using Newtonsoft.Json;
using System.Net.Http;

public class AppManager : MonoBehaviour
{
    private string url;
    private UnityWebRequest unityWebRequest;
    [SerializeField] private FileGetter fileGetter_Ref;

    public enum State { _1st_Column, _2nd_1_Column, _2nd_2_Column , _3rd_Column, Tab2_AgeFilter, Tab3_Styles };

    public State currentState = State._1st_Column;

    public enum Tabs { RestoredFace, AgeFilter, Styles };

    public Tabs currentTab = Tabs.RestoredFace;

    [Header("Tab Buttons")]
    [SerializeField] private Button restoredFace, ageFilter, styles_Embeddings; // Tab1,Tab2,Tab3 respectively

    [Header("Tabs")]
    [SerializeField] private GameObject restoredFace_Holder, ageFilter_Holder, styles_Holder; // Tab1,Tab2,Tab3 respectively

    /// <summary>
    /// Restored Face
    /// </summary>
    ///
    [Header("Tab 1 Steps")]
    [SerializeField] private GameObject tab1_step1, tab1_step2, tab1_step3;

    /// <summary>
    /// Step1 Fileds
    /// </summary>
    ///
    [Header("Tab 1 Step 1")]
    [SerializeField] private RawImage _1stColumnImage;
    [SerializeField] private TMP_Text _1stColumn_Name;
    [SerializeField] private TMP_Text _1stColumn_Age;
    [SerializeField] private TMP_Text _1stColumn_Status;
    private byte[] loadedTextureData;

    /// <summary>
    /// Step2 Fileds
    /// </summary>
    /// 
    [Header("Tab 1 Step 2")]
    [SerializeField] private RawImage _2nd_1_ColumnImage;
    [SerializeField] private RawImage _2nd_2_ColumnImage;
    private string _2nd_1_ColumnImage_path = "";
    private string _2nd_2_ColumnImage_path = "";
    private Action column2_response_search_offline_callback;
    private Action column2_response_search_online_callback;


    /// <summary>
    /// Step3 Fileds
    /// </summary>
    ///
    [Header("Tab 1 Step 3")]
    [SerializeField] private GameObject toInstantiate;
    [SerializeField] private Transform step3_Root;
    [SerializeField] private GameObject step3_Title,step3_AdditionalInfo;




    /// <summary>
    /// Restored Face
    /// </summary>
    ///
    [Header("Tab 1 Steps")]
    [SerializeField] private GameObject tab2_step2, tab2_step3, tab3_step3;

    /// <summary>
    /// Age Filter
    /// </summary>
    ///
    [Header("Tab 2")]
    [SerializeField] private Toggle detectedFace_Toggle, restoredFace_Toggle;
    [SerializeField] private Button detectedFace_Toggle_Button, restoredFace_Toggle_Button;
    [SerializeField] private string pathOfimageSelected_AgeFilter = "";
    [SerializeField] private string pathOfimageSelected_ageFilter_Embeddings = "";

    [SerializeField] private Button previous_ageFilter_Button, next_ageFilter_Button, ageFilter_rawImage_Button,ageFilter_Embeddings_Back_Button;
    [SerializeField] private TMP_Text ageFilter_Text;
    [SerializeField] private int max_Age, min_Age,currentselectedAge, incrementValue;
    [SerializeField] private RawImage ageFilter_rawImage;


    /// <summary>
    /// Hair
    /// </summary>
    ///

    [SerializeField] private Toggle[] hairStyleToggles;
    [SerializeField] private RawImage haristyle;

    [SerializeField] private GameObject loader;
    private string Log_Type = "AppManager";

    public static AppManager appManagerInstance;

    private void Awake()
    {
        appManagerInstance = this;
    }

    // Start is called before the first frame update
    void Start()
    {
        //System.Diagnostics.Process.Start("WinRAR.exe", @"C:\Program Files\WinRAR");

        //SendData();

        //var dat1 = new EmbeddingsSearch();

        //dat1.path = "1";
        //dat1.searchType = "1";

        //var data = JsonUtility.ToJson(dat1);

        //File.WriteAllText(Path.Combine(Application.streamingAssetsPath, "myjson.json"), data);

        var path = Path.Combine(Application.streamingAssetsPath, "IP_Address.txt");

        Debug.Log(Log_Type + " Start " + File.ReadAllText(path));

        url = File.ReadAllText(path);

        // Add listeners to column2, detectedface and restored face
        AddListenterToColumn2();

        // Tabs Initialization
        restoredFace.interactable = true;
        restoredFace.GetComponent<Outline>().enabled = true;
        ageFilter.interactable = false;
        styles_Embeddings.interactable = false;

        foreach(var toggle in hairStyleToggles)
        {
            toggle.transform.GetChild(2).GetComponent<Button>().onClick.AddListener(delegate
            {
                foreach (var toggle1 in hairStyleToggles)
                {
                    toggle1.isOn = false;
                }

                toggle.isOn = true;

                HairStyleToggles(toggle.transform.GetChild(1).GetComponent<Text>().text);
            });
        }

        restoredFace.GetComponent<Button>().onClick.AddListener(delegate
        {
            if (!restoredFace.GetComponent<Outline>().enabled)
            {
                TabSwitch(Tabs.RestoredFace);
            }
        });

        ageFilter.GetComponent<Button>().onClick.AddListener(delegate
        {
            if (!ageFilter.GetComponent<Outline>().enabled)
            {
                TabSwitch(Tabs.AgeFilter);
            }

        });

        styles_Embeddings.GetComponent<Button>().onClick.AddListener(delegate
        {
            if (!styles_Embeddings.GetComponent<Outline>().enabled)
            {
                TabSwitch(Tabs.Styles);
            }

        });

        // Age Filter Initialization

        detectedFace_Toggle_Button.onClick.AddListener(delegate
        {
            detectedFace_Toggle.isOn = true;
            restoredFace_Toggle.isOn = false;

            ageFilter_Embeddings_Back_Button.onClick.Invoke();

            currentselectedAge = 50;

            ToggleHandler(0); // Detected face

            AgeModification(0);
        });

        restoredFace_Toggle_Button.onClick.AddListener(delegate
        {
            detectedFace_Toggle.isOn = false;
            restoredFace_Toggle.isOn = true;

            ageFilter_Embeddings_Back_Button.onClick.Invoke();

            currentselectedAge = 50;

            ToggleHandler(1); // Restored face

            AgeModification(0);
        });

        previous_ageFilter_Button.onClick.AddListener(delegate
        {
            AgeModification(0);
        });

        next_ageFilter_Button.onClick.AddListener(delegate
        {
            AgeModification(1);
        });

        ageFilter_rawImage_Button.onClick.AddListener(delegate
        {
            ModalManager.Show("Are you sure?", "It will fetch the Embeddings.", new[] { new ModalButton() { Text = "Search Offline", Callback = column2_response_search_offline_callback }, new ModalButton() { Text = "Search Online", Callback = column2_response_search_online_callback }, new ModalButton() { Text = "Cancel" } });
        });

        ageFilter_Embeddings_Back_Button.onClick.AddListener(delegate
        {
            tab1_step3.SetActive(false);
            tab2_step3.SetActive(true);

            ageFilter_Embeddings_Back_Button.gameObject.SetActive(false);
        });

        AgeModification(0,""); //Default Call
    }

    private void OnEnable()
    {
        column2_response_search_offline_callback += GetConfirmationResponse_Offline;
        column2_response_search_online_callback += GetConfirmationResponse_Online;
    }

    private void OnDisable()
    {
        column2_response_search_offline_callback -= GetConfirmationResponse_Offline;
        column2_response_search_online_callback -= GetConfirmationResponse_Online;
    }

    #region Tabs

    private void TabSwitch(Tabs currentTab)
    {
        restoredFace.GetComponent<Outline>().enabled = false;
        ageFilter.GetComponent<Outline>().enabled = false;
        styles_Embeddings.GetComponent<Outline>().enabled = false;

        switch (currentTab)
        {
            case Tabs.RestoredFace: // Enable step1,step2 and step3 of Tab1

                currentState = State._1st_Column;

                restoredFace.GetComponent<Outline>().enabled = true;

                ageFilter_Holder.SetActive(false);
                styles_Holder.SetActive(false);

                AddListenterToColumn2();
                tab1_step3.SetActive(true);
                tab3_step3.SetActive(false);
                tab2_step3.SetActive(false);

                step3_AdditionalInfo.GetComponent<TMP_Text>().text = "";

                step3_Title.SetActive(false);

                // Destroy all the items
                for (var i = 0; i < step3_Root.childCount; i++)
                {
                    Destroy(step3_Root.GetChild(i).gameObject);
                }

                styles_Embeddings.interactable = false;

                break;
            case Tabs.AgeFilter: // Enable step1,step2 of Tab1 and new step3 enabled it
                ageFilter.GetComponent<Outline>().enabled = true;

                //Disable Tab1 Step3 first
                tab1_step3.SetActive(false);
                tab3_step3.SetActive(false);
                RemoveListenterToColumn2(); // Remove listeners so that the modal window will not be shown
                ageFilter_Holder.SetActive(true);

                pathOfimageSelected_AgeFilter = _2nd_1_ColumnImage_path;

                ageFilter_rawImage.texture = null;
                ageFilter_Embeddings_Back_Button.gameObject.SetActive(false);
                tab2_step3.SetActive(true);

                detectedFace_Toggle_Button.onClick.Invoke();

                styles_Embeddings.interactable = true;

                break;
            case Tabs.Styles:
                foreach (var toggle1 in hairStyleToggles)
                {
                    toggle1.isOn = false;
                }

                haristyle.texture = null;

                styles_Embeddings.GetComponent<Outline>().enabled = true;
                tab3_step3.SetActive(true);
                tab1_step3.SetActive(false);
                tab2_step3.SetActive(false);


                break;
            default:
                break;
        }
    }

    #endregion

    #region Restored face

    #region Step1

    public void OpenFileExplorer()
    {
        if(currentState != State.Tab2_AgeFilter)
        {
            // Coroutine example
            fileGetter_Ref.StartCoroutine("ShowLoadDialogCoroutine");
        }
        else
        {
            ModalManager.Show("Go to Restored Image Tab", "Go to the restored face tab, to change the image", new[] { new ModalButton() { Text = "OK" } });
        }

    }

    /// <summary>
    /// 
    /// </summary>
    /// <param name="path"></param>
    /// <param name="currentState"></param>
    /// <returns></returns>
    public IEnumerator ReadTheImage(string path, State currentState, JsonData_Embeddings_Data jsonData = null)
    {
        using (UnityWebRequest uwr = UnityWebRequestTexture.GetTexture(path))
        {
            yield return uwr.SendWebRequest();

            if (uwr.result != UnityWebRequest.Result.Success)
            {
                Debug.Log(uwr.error);
            }
            else
            {
                var texture = DownloadHandlerTexture.GetContent(uwr);

                loadedTextureData = texture.EncodeToJPG();

                switch (currentState)
                {
                    case State._1st_Column:
                        _1stColumnImage.texture = texture;

                        var data = this.GetComponent<CSVParsing>().ReturnAdditionInfo(Path.GetFileName(path));

                        ResetTheData();


                        if (data.Length == 0)
                        {
                            // Showcase an alert mentioning that, no relevanr data is retrieved

                            _1stColumn_Name.text = "NA";
                            _1stColumn_Age.text = "NA";
                            _1stColumn_Status.text = "NA";

                            ModalManager.Show("No Addition Data", "No corresponding data is available in the excel sheet.", new[] { new ModalButton() { Text = "OK" } });
                        }
                        else
                        {
                            _1stColumn_Name.text = data[0];
                            _1stColumn_Age.text = data[1];
                            _1stColumn_Status.text = data[2];

                            if (data[2].Equals("Traced"))
                            {
                                ModalManager.Show("Already Traced", "Missing person is already traced out.", new[] { new ModalButton() { Text = "OK" } });
                            }
                            else
                            {
                                AppManager.appManagerInstance.SendDataToFlask(path); // send to flask
                            }
                        }

                        break;
                    case State._2nd_1_Column:
                        _2nd_1_ColumnImage.texture = texture;
                        break;
                    case State._2nd_2_Column:
                        _2nd_2_ColumnImage.texture = texture;
                        break;
                    case State._3rd_Column:

                        // Add the images

                        var obj = GameObject.Instantiate(toInstantiate, step3_Root, false);
                        obj.GetComponent<RawImage>().texture = texture;

                        obj.name = jsonData.fileName;

                        obj.GetComponent<Button>().onClick.AddListener(delegate
                        {
                            ChangeTheOutlineAndDisplayAdditinalInfo(jsonData);

                            obj.GetComponent<Outline>().enabled = true;

                        });

                        break;
                    case State.Tab2_AgeFilter:

                        ageFilter_rawImage.texture = texture;

                        break;

                    case State.Tab3_Styles:

                        haristyle.texture = texture;

                        break;
                }
            }
        }
    }

    public async void SendDataToFlask(string filepath)
    {
        using (var httpClient = new HttpClient())
        {
            httpClient.Timeout = TimeSpan.FromSeconds(1000 * 60 * 5); // 5 mins

            loader.SetActive(true);

            using HttpResponseMessage response = await httpClient.PostAsync((url + "/SendimageFilePath"), new StringContent ( filepath ));
            response.EnsureSuccessStatusCode();
            string responseBody = await response.Content.ReadAsStringAsync();

            Debug.Log(Log_Type + " SendDataToFlask API Response " + responseBody);

            StartCoroutine(GetTheAnalysedImages(responseBody.Split(','), "2ndColumn"));

            loader.SetActive(false);
        }
    }

    /// <summary>
    /// Gets the analysed Images
    /// </summary>
    /// <param name="paths"></param>
    /// <param name="column"></param>
    /// <returns></returns>
    private IEnumerator GetTheAnalysedImages(string[] paths,string column)
    {
        if(column.Equals("2ndColumn"))
        {
            currentState = State._2nd_1_Column;

            var coroutine = StartCoroutine(ReadTheImage(paths[0], currentState));

            _2nd_1_ColumnImage_path = paths[0];

            yield return coroutine;

            currentState = State._2nd_2_Column;

            StartCoroutine(ReadTheImage(paths[1], currentState));

            _2nd_2_ColumnImage_path = paths[1];

            yield return coroutine;

            // Make the 2nd Tab Interactable
            ageFilter.interactable = true;

        }
        else if(column.Equals("3rdColumn"))
        {
            currentState = State._3rd_Column;

            // Add a foreach to get all the images
            var jsonString = File.ReadAllText(paths[0]);

            step3_Title.SetActive(true);

            step3_AdditionalInfo.SetActive(true);

            Debug.Log(Log_Type + " GetTheEmbeddings : jsonString " + jsonString);

            var jsonObject = JsonUtility.FromJson<JsonData_Embeddings>(jsonString);

            Debug.Log(Log_Type + " GetTheEmbeddings : jsonObject " + jsonObject.jsonData_Embeddings_Data);

            foreach (var element in jsonObject.jsonData_Embeddings_Data)
            {
                var coroutine = StartCoroutine(ReadTheImage(element.Path, currentState, element));

                yield return coroutine;
            }
        }
        else if(column.Equals("Tab2_AgeFilter"))
        {
            currentState = State.Tab2_AgeFilter;

            var coroutine = StartCoroutine(ReadTheImage(paths[0], currentState));

            yield return coroutine;
        }
        else if (column.Equals("Tab3_Styles"))
        {
            currentState = State.Tab3_Styles;

            var coroutine = StartCoroutine(ReadTheImage(paths[0], currentState));

            yield return coroutine;
        }
    }

    #endregion

    #region Step2


    private void AddListenterToColumn2()
    {
        _2nd_1_ColumnImage.GetComponent<Button>().onClick.AddListener(delegate
        {
            ModalManager.Show("Are you sure?", "It will fetch the Embeddings.", new[] { new ModalButton() { Text = "Search Offline", Callback = column2_response_search_offline_callback }, new ModalButton() { Text = "Search Online", Callback = column2_response_search_online_callback }, new ModalButton() { Text = "Cancel" } });

        });

        _2nd_2_ColumnImage.GetComponent<Button>().onClick.AddListener(delegate
        {
            ModalManager.Show("Are you sure?", "It will fetch the Embeddings.", new[] { new ModalButton() { Text = "Search Offline", Callback = column2_response_search_offline_callback }, new ModalButton() { Text = "Search Online", Callback = column2_response_search_online_callback }, new ModalButton() { Text = "Cancel" } });

        });
    }

    private void RemoveListenterToColumn2()
    {
        _2nd_1_ColumnImage.GetComponent<Button>().onClick.RemoveAllListeners();

        _2nd_2_ColumnImage.GetComponent<Button>().onClick.RemoveAllListeners();
    }

    private void GetConfirmationResponse_Offline()
    {
        step3_AdditionalInfo.GetComponent<TMP_Text>().text = "";

        // Destroy all the items
        for (var i = 0; i < step3_Root.childCount; i++)
        {
            Destroy(step3_Root.GetChild(i).gameObject);
        }


        if (currentState == State.Tab2_AgeFilter)
        {
            tab1_step3.SetActive(true);
            tab2_step3.SetActive(false);

            ageFilter_Embeddings_Back_Button.gameObject.SetActive(true);

            GetTheEmbeddings(pathOfimageSelected_ageFilter_Embeddings, "Search_Offline");
        }
        else
        {
            GetTheEmbeddings(_2nd_1_ColumnImage_path, "Search_Offline");
        }
    }

    private void GetConfirmationResponse_Online()
    {
        step3_AdditionalInfo.GetComponent<TMP_Text>().text = "";

        // Destroy all the items
        for (var i = 0; i < step3_Root.childCount; i++)
        {
            Destroy(step3_Root.GetChild(i).gameObject);
        }


        if (currentState == State.Tab2_AgeFilter)
        {
            tab1_step3.SetActive(true);
            tab2_step3.SetActive(false);

            ageFilter_Embeddings_Back_Button.gameObject.SetActive(true);

            GetTheEmbeddings(pathOfimageSelected_ageFilter_Embeddings, "Search_Online");
        }
        else
        {
            GetTheEmbeddings(_2nd_1_ColumnImage_path, "Search_Online");
        }
    }

    public async void GetTheEmbeddings(string path,string typeOfSearch)
    {
        if(!string.IsNullOrEmpty(path))
        {
            using (var httpClient = new HttpClient())
            {
                httpClient.Timeout = TimeSpan.FromSeconds(1000 * 60 * 5); // 5 mins

                var data = new EmbeddingsSearch();

                data.path = path;
                data.searchType = typeOfSearch;

                var jsonString = JsonUtility.ToJson(data);

                loader.SetActive(true);

                using HttpResponseMessage response = await httpClient.PostAsync((url + "/SendimageFilePath_Embedding"), new StringContent(jsonString));
                response.EnsureSuccessStatusCode();
                string responseBody = await response.Content.ReadAsStringAsync();

                Debug.Log(Log_Type + " GetTheEmbeddings : API Response " + responseBody);

                StartCoroutine(GetTheAnalysedImages(new string[] { responseBody }, "3rdColumn"));

                loader.SetActive(false);
            }
        }
        else
        {
            Debug.Log(Log_Type + " GetTheEmbeddings path is empty ");
        }
    }

    #endregion

    #region Step3

    public void ChangeTheOutlineAndDisplayAdditinalInfo(JsonData_Embeddings_Data selectedObjectName)
    {
        // Destroy all the items
        for (var i = 0; i < step3_Root.childCount; i++)
        {
            step3_Root.GetChild(i).GetComponent<Outline>().enabled = false;
        }

        step3_AdditionalInfo.GetComponent<TMP_Text>().text = "Distance" + " : " + selectedObjectName.Confidence + System.Environment.NewLine +
            "Source" + " : " + selectedObjectName.Source + System.Environment.NewLine +
            "AdditionalInfo" + " : " + selectedObjectName.AdditionalInfo;
    }

    #endregion

    #endregion

    #region AgeFilter
    /// <summary>
    /// If value = 0, it's detected image, else, it's restored image
    /// </summary>
    /// <param name="value"></param>
    private void ToggleHandler(int value)
    {
        if(value == 0)
        {
            pathOfimageSelected_AgeFilter = _2nd_1_ColumnImage_path;
        }
        else
        {
            pathOfimageSelected_AgeFilter = _2nd_2_ColumnImage_path;
        }
    }

    /// <summary>
    /// If value is 0, previous button pressed, or else it's next button
    /// </summary>
    /// <param name="value"></param>
    public void AgeModification(int value, string callAPI = "yes")
    {

        if(value == 0)
        {
            currentselectedAge -= incrementValue;
        }
        else
        {
            currentselectedAge += incrementValue;
        }
        if (currentselectedAge <= min_Age)
        {
            previous_ageFilter_Button.interactable = false;
            currentselectedAge = min_Age;
            next_ageFilter_Button.interactable = true;
        }
        else if (currentselectedAge >= max_Age)
        {
            next_ageFilter_Button.interactable = false;
            currentselectedAge = max_Age;
            previous_ageFilter_Button.interactable = true;
        }
        else
        {
            previous_ageFilter_Button.interactable = true;
            next_ageFilter_Button.interactable = true;
        }

        ageFilter_Text.text = "Age : " + currentselectedAge.ToString();

        if(callAPI.Equals("yes"))
        {
            // Call the api
            AgeFilterAPI(pathOfimageSelected_AgeFilter, currentselectedAge);
        }
    }

    public async void AgeFilterAPI(string filepath,int age)
    {
        //{ "path":"1","age":"1"}

        var data = new AgeFilter();

        data.path = filepath;
        data.age = age.ToString();

        var jsonString = JsonUtility.ToJson(data);

        using (var httpClient = new HttpClient())
        {
            httpClient.Timeout = TimeSpan.FromSeconds(1000 * 60 * 5); // 5 mins

            loader.SetActive(true);

            using HttpResponseMessage response = await httpClient.PostAsync((url + "/SendimageFilePath_age"), new StringContent(jsonString));
            response.EnsureSuccessStatusCode();
            string responseBody = await response.Content.ReadAsStringAsync();

            Debug.Log(Log_Type + " SendDataToFlask API Response " + responseBody);

            pathOfimageSelected_ageFilter_Embeddings = responseBody;

            StartCoroutine(GetTheAnalysedImages(new string[] { responseBody }, "Tab2_AgeFilter"));

            loader.SetActive(false);
        }
    }

    #endregion

    #region Hair

    private void HairStyleToggles(string selectedHairStyle)
    {
        HairStyleAPI(pathOfimageSelected_AgeFilter, selectedHairStyle);
    }

    public async void HairStyleAPI(string filepath, string selectedHairStyle)
    {
        //{ "path":"1","age":"1"}

        var data = new HaiStyle();

        data.path   = filepath;
        data.style  = selectedHairStyle;

        var jsonString = JsonUtility.ToJson(data);

        using (var httpClient = new HttpClient())
        {
            httpClient.Timeout = TimeSpan.FromSeconds(1000 * 60 * 5); // 5 mins

            loader.SetActive(true);

            using HttpResponseMessage response = await httpClient.PostAsync((url + "/SendimageFilePath_hair"), new StringContent(jsonString));
            response.EnsureSuccessStatusCode();
            string responseBody = await response.Content.ReadAsStringAsync();

            Debug.Log(Log_Type + " HairStyleAPI API Response " + responseBody);

            pathOfimageSelected_ageFilter_Embeddings = responseBody;

            StartCoroutine(GetTheAnalysedImages(new string[] { responseBody }, "Tab3_Styles"));

            loader.SetActive(false);
        }
    }

#endregion

    #region Helpers

    private void ResetTheData()
    {
        currentState = State._1st_Column;

        //Tabs
        restoredFace.interactable = true;
        ageFilter.interactable = false;
        styles_Embeddings.interactable = false;

        restoredFace.GetComponent<Outline>().enabled = true;
        ageFilter.GetComponent<Outline>().enabled = false;
        styles_Embeddings.GetComponent<Outline>().enabled = false;

        // Reset Tab1 2nd column
        _2nd_1_ColumnImage.texture = null;
        _2nd_2_ColumnImage.texture = null;
        _2nd_1_ColumnImage_path = "";
        _2nd_2_ColumnImage_path = "";

        currentState = State._1st_Column;

        // Reset Tab1 3rd Column

        step3_Title.SetActive(false);

        step3_AdditionalInfo.GetComponent<TMP_Text>().text = "";

        step3_AdditionalInfo.SetActive(false);

        // Tab2 
        currentselectedAge = 50;
        detectedFace_Toggle.isOn = true;
        restoredFace_Toggle.isOn = false;
        pathOfimageSelected_AgeFilter = "";
        pathOfimageSelected_ageFilter_Embeddings = "";
        ageFilter_rawImage.texture = null;

        AgeModification(0, "");

        foreach (var toggle1 in hairStyleToggles)
        {
            toggle1.isOn = false;
        }

        haristyle.texture = null;

        // Destroy all the items
        for (var i=0;i< step3_Root.childCount;i++)
        {
            Destroy(step3_Root.GetChild(i).gameObject);
        }
    }
    #endregion

    [Serializable]
    public class JsonData_Embeddings
    {
        public List<JsonData_Embeddings_Data> jsonData_Embeddings_Data = new List<JsonData_Embeddings_Data>();
    }


    [Serializable]
    public class JsonData_Embeddings_Data
    {
        public string fileName;
        public string Path;
        public string Confidence;
        public string Source;
        public string AdditionalInfo;
    }

    [Serializable]
    public class HaiStyle
    {
        public string path;
        public string style;
    }

    [Serializable]
    public class EmbeddingsSearch
    {
        public string path;
        public string searchType;
    }

    [Serializable]
    public class AgeFilter
    {
        public string path;
        public string age;
    }
}
