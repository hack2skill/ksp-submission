const missingPerson = require('./missingPersonSchema')

const insertMissingPersonDetail = (District_Name, UnitName, FIRNo, RI, Year, Month, Offence_From_Date, Offence_To_Date, FIR_Date, FIR_Type, FIR_Stage, CrimeGroup_Name, CrimeHead_Name, ActSection, Photo_Full_front, Gender, Person_Name, age_yr, age_month, age_day) => {

    return new Promise((resolve, reject) => {

        const person = new missingPerson({
            District_Name,
            UnitName, FIRNo, RI, Year, Month, Offence_From_Date, Offence_To_Date, FIR_Date, FIR_Type, FIR_Stage, CrimeGroup_Name, CrimeHead_Name, ActSection, Photo_Full_front, Gender, Person_Name,
            Person_Age: [{
                years: age_yr,
                months: age_month,
                days: age_day
            }]
        })
        person.save()
            .then((msg) => {
                console.log(msg)
                resolve(`Added person with name ${Person_Name}`)
            })
            .catch((err) => {
                console.log(`- - - - - Couln't add person - - - - -`)
                console.log(err)
                reject(`Couldn't add person`)
            })

    })

}

const getMissingPersonDetailByImageName = async (imageName) => {
    console.log('here')
    const personDetail = await missingPerson.find({ Photo_Full_front: imageName })
    // console.log(personDetail)
    return new Promise((resolve, reject) => {
        if(personDetail) resolve(personDetail)
        else reject()
    })
    
}

module.exports = {
    insertMissingPersonDetail,
    getMissingPersonDetailByImageName
}