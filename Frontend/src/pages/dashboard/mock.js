const userConstants = {
  bigStat: [
    {
      product: "Light Blue",
      total: {
        monthly: 4232,
        weekly: 1465,
        daily: 199,
        percent: { value: 3.7, profit: false }
      },
      color: "primary",
      registrations: {
        monthly: { value: 830, profit: false },
        weekly: { value: 215, profit: true },
        daily: { value: 33, profit: true }
      },
      bounce: {
        monthly: { value: 4.5, profit: false },
        weekly: { value: 3, profit: true },
        daily: { value: 3.25, profit: true }
      }
    },
    {
      product: "Sing App",
      total: {
        monthly: 754,
        weekly: 180,
        daily: 27,
        percent: { value: 2.5, profit: true }
      },
      color: "warning",
      registrations: {
        monthly: { value: 32, profit: true },
        weekly: { value: 8, profit: true },
        daily: { value: 2, profit: false }
      },
      bounce: {
        monthly: { value: 2.5, profit: true },
        weekly: { value: 4, profit: false },
        daily: { value: 4.5, profit: false }
      }
    },
    {
      product: "RNS",
      total: {
        monthly: 1025,
        weekly: 301,
        daily: 44,
        percent: { value: 3.1, profit: true }
      },
      color: "secondary",
      registrations: {
        monthly: { value: 230, profit: true },
        weekly: { value: 58, profit: false },
        daily: { value: 15, profit: false }
      },
      bounce: {
        monthly: { value: 21.5, profit: false },
        weekly: { value: 19.35, profit: false },
        daily: { value: 10.1, profit: true }
      }
    }
  ],
  notifications: [
    {
      id: 0,
      icon: "thumbs-up",
      color: "primary",
      content:
        'Ken <span className="fw-semi-bold">accepts</span> your invitation'
    },
    {
      id: 1,
      icon: "file",
      color: "success",
      content: "Report from LT Company"
    },
    {
      id: 2,
      icon: "envelope",
      color: "danger",
      content: '4 <span className="fw-semi-bold">Private</span> Mails'
    },
    {
      id: 3,
      icon: "comment",
      color: "success",
      content: '3 <span className="fw-semi-bold">Comments</span> to your Post'
    },
    {
      id: 4,
      icon: "cog",
      color: "light",
      content: 'New <span className="fw-semi-bold">Version</span> of RNS app'
    },
    {
      id: 5,
      icon: "bell",
      color: "info",
      content:
        '15 <span className="fw-semi-bold">Notifications</span> from Social Apps'
    }
  ],
  table: [
    {
      "_index": "fir_new",
      "_id": "732651b5-543f-42ff-84e8-6d3ca8ccaab2",
      "_score": 44.60634,
      "_source": {
        "State": "Bihar",
        "Unit_ID": 1567,
        "PersonStatus": "Arrested&sent to JC",
        "Minor_Head": "Electronic Goods (Radio,TV,VCR,ACs,Office Automation Equipments)",
        "Arr_ID": 2022000866,
        "District_Name": "Patna",
        "Major_Head": "THEFT/Electronic Goods (Radio,TV,VCR,ACs,Office Automation Equipments)",
        "Crime_No": 10440156720220009,
        "Father_Name": "YAMANURASAB",
        "Gender": "M",
        "FIRNo": "0009/2022",
        "AgeWhileOpening": 23,
        "Person_No": "A3",
        "Age": 23,
        "FIR_ID": 2022000013,
        "DEDT": "2022-07-14T14:09:18.287000",
        "Person_Name": "FAKKIRASAB YAMANURSAB MULIMANI",
        "Perm_Address1": "AT: MEVUNDI,TQ-MUNDARAGI Gadag Karnataka",
        "FIR_Date": "2022-01-09T00:00:00",
        "PS_Name": "Kankerbagh Police Station",
        "Pres_Address1": "AT: MEVUNDI,TQ: MUNDARAGI Gadag Karnataka",
        "Arrest_Date": "2022-01-10T00:00:00",
        "Name": "YAMANURASAB"
      }
    },
    {
      "_index": "fir_new",
      "_id": "0d0f841b-7dbc-426c-beae-b3220f069559",
      "_score": 44.60634,
      "_source": {
        "State": "Sikkim",
        "Unit_ID": 1567,
        "PersonStatus": "Arrested",
        "Minor_Head": "Electronic Goods (Radio,TV,VCR,ACs,Office Automation Equipments)",
        "Arr_ID": 2022000863,
        "District_Name": "Gangtok",
        "Major_Head": "THEFT/Electronic Goods (Radio,TV,VCR,ACs,Office Automation Equipments)",
        "Crime_No": 10440156720220009,
        "Father_Name": null,
        "Gender": "M",
        "FIRNo": "0009/2022",
        "AgeWhileOpening": 23,
        "Person_No": "A3",
        "Age": 23,
        "FIR_ID": 2022000013,
        "DEDT": "2022-07-14T13:53:26.010000",
        "Person_Name": "FAKKIRASAB YAMANURSAB MULIMANI",
        "Perm_Address1": null,
        "FIR_Date": "2022-01-09T00:00:00",
        "PS_Name": "Development Area Police Station",
        "Pres_Address1": "AT: MEVUNDI,TQ: MUNDARAGI Gadag Karnataka",
        "Arrest_Date": null,
        "Name": null
      }
    }
  ]
};
export default userConstants;