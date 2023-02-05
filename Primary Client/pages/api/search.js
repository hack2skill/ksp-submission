import axios from "axios";

export default async function handler(req, res) {
  let cookies;
  let r;

  axios.defaults.baseURL = process.env.PORTAL_URL;

  r = await axios.get("/login", {
    headers: {
      Accept: "text/html",
    },
  });

  const cheerio = require("cheerio");
  const htmlparser2 = require("htmlparser2");
  let dom = htmlparser2.parseDocument(r.data);

  let $ = cheerio.load(dom);

  const csrf = $("input[name=_token]").attr("value");
  cookies = r.headers["set-cookie"].map((cookie) => cookie.split(";")[0]);

  r = await axios.post(
    "/login",
    {
      email: "test@gmail.com",
      password: "12345678",
      _token: csrf,
    },
    {
      headers: {
        Cookie: cookies.join("; "),
      },
    }
  );

  cookies = r.headers["set-cookie"].map((cookie) => cookie.split(";")[0]);

  r = await axios.get("/search", {
    params: req.query,
    headers: {
      Cookie: cookies.join("; "),
      Accept:
        "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    },
  });

  var JSSoup = require("jssoup").default;

  var soup = new JSSoup(r.data);
  let icjs_array = [];

  soup.findAll("tr").forEach((t) => {
    let content_object = {};
    let headers = [
      "State",
      "District_Name",
      "PS_Name",
      "FIRNo",
      "FIR_Date",
      "Person_No",
      "Arrest_Date",
      "Person_Name",
      "Father_Name",
      "Gender",
      "AgeWhileOpening",
      "Age",
      "Pres_Address1",
      "Perm_Address1",
      "PersonStatus",
      "Name",
      "Major_Head",
      "Minor_Head",
      "Crime_No",
      "Arr_ID",
      "Unit_ID",
      "FIR_ID",
      "DEDT",
    ];

    t.contents.forEach((c, index) => {
      content_object[headers[index]] = c.contents.toString();
    });
    icjs_array.push(content_object);
  });

  delete icjs_array[0];

  const token = (
    await axios.post("/api/login", {
      email: "test@gmail.com",
      password: "12345678",
    })
  ).data.token;

  const state_array = (
    await axios.get("/api/search", {
      params: req.query,
      headers: {
        Authorization: `Bearer ${token}`,
      },
    })
  ).data.data.data;

  let both = [];

  icjs_array.forEach((p, p_index) => {
    let q_i;

    state_array.forEach((q, q_index) => {
      if (
        p["Arr ID"] === q["Arr_ID"] ||
        (p["Person Name"] === q["Person_Name"] &&
          (p["Father Name"] === q["Father_Name"] ||
            p["Perm Address1"] === q["Perm_Address1"]))
      ) {
        q_i = true;
        delete state_array[q_index];
      }
    });

    if (q_i) {
      both.push(p);
      delete icjs_array[p_index];
    }
  });

  let final = [];

  icjs_array.forEach((p) => final.push({ ...p, type: "icjs" }));
  state_array.forEach((p) => final.push({ ...p, type: "state" }));
  both.forEach((p) => final.push({ ...p, type: "both" }));

  return res.status(200).json({ data: final });
}
