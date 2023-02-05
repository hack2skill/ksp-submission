import pandas as pd
from pymongo import MongoClient
from bson.binary import Binary
import pickle
from pprint import pprint
from Constants import const
from Scripts.Utility import utils
import numpy as np



class MongoConn:
    def __init__(self, server):
        # self.mongo_atlas_srv = utils.configuration["mongodb_credentials"]["mongodb_url_production"]
        # self.client = MongoClient(self.mongo_atlas_srv)
        # self.db = self.client[utils.configuration["mongodb_credentials"]["database_production"]]

        self.mongo_atlas_srv = utils.configuration["mongodb_credentials"]["mongodb_url"]
        self.client = MongoClient(self.mongo_atlas_srv)
        self.db = self.client[utils.configuration["mongodb_credentials"]["database"]]

# ***********************************************************************************************************************************************************************************************
# ***********************************************************************************************************************************************************************************************
# ***********************************************************************************************************************************************************************************************
# ***********************************************************************************************************************************************************************************************
# ***********************************************************************************************************************************************************************************************

    """   
                                                          INSERTING / UPDATING INTO MONGO DATABASE
    
    """
    #------------------------------------------- Inserting Documents into Table_1 --------------------------------------

    def insert_profileImageVector_into_Table_1(self, update_profile_table1):
        '''
        Insert Binary numpy array of profile images along with other data into Table_1.
        # ConnectionErrorConvert numpy array to Binary, store record in mongodb
        '''
        try:
            update_profile_table1['profile_image_embedding'] = Binary(pickle.dumps(update_profile_table1['profile_image_embedding'], protocol=2), subtype=128)

            self.db[const.table1_profileVectorizedImages].update_one(filter={  'user_id': update_profile_table1['user_id'],
                                                                               'profile_image_s3key': update_profile_table1['profile_image_s3key'],
                                                                               'type': update_profile_table1['type'],
                                                                               'is_dp': update_profile_table1['is_dp'],
                                                                               'gender': update_profile_table1['gender']
                                                                             },
                                                                    update={"$set": {'user_id': update_profile_table1['user_id'],
                                                                               'profile_image_s3key': update_profile_table1['profile_image_s3key'],
                                                                               'type': update_profile_table1['type'],
                                                                               'is_dp': update_profile_table1['is_dp'],
                                                                               'gender': update_profile_table1['gender'],
                                                                               'profile_image_embedding': update_profile_table1['profile_image_embedding']}
                                                                      },
                                                                    upsert=True)

            return {"status" : 1, "message": const.table1_profileVectorizedImages + " is updated"}

        except Exception as e:
            utils.logger.error("Exception occurred while inserting image vectors of profile image into Table_1 : " + str(e))
            return {"status": -1, "message": const.table1_profileVectorizedImages + " is NOT updated"}

        # ------------------------------------------- Inserting Documents into table_2 -------------------------------------

    def push_newProfileImgVector_into_matchedUsersArray_table2(self, push_profile_table2):
        '''
        Insert matched users list with percentage match along with other details into Table_2.
        This is updated/pushed only when a user adds a new profile images(whether DP or not DP) or a new user sign up and then add his profile image(s).
        Idea is to find match of this "new profile image" w.r.t. all the "preference_images" in Table#2, calculate distances and append into the list.
        ```
            for item in Table#2 :
                if ( gender(item[user_id] ) != gender(new_image) && (gender(item[preference_image] ) == gender(new_profile_image)) ):
                    dist = CalculateDistance( item[preference_image_vector], new_profile_image_vector )
                    Table#2[item].add( dist, new_profile_image )
        ```
        In this table we have 'user_id' and 'preference_image_id' are primary key.
        '''
        try:
            # push_data_matched_users_array_table2['preference_image_embedding'] = Binary(pickle.dumps(push_data_matched_users_array_table2['preference_image_embedding'], protocol=2), subtype=128)

            for item in self.db[const.table2_preferencesBasedMatchedProfiles].find():
                print(item)
                item_gender = list(self.db[const.table1_profileVectorizedImages].find({"user_id": item["user_id"]}))[0]["gender"]

                # if ("sexual_orientation == "Straight")
                if item_gender != push_profile_table2["gender"]:
                    img_embedding2 = pickle.loads(item["preference_image_embedding"])
                    img_embedding1 = pickle.loads(push_profile_table2["profile_image_embedding"])

                    dist = np.linalg.norm(img_embedding2 - img_embedding1)      # Geometrical Distance between Images
                    dist = float(dist)                                          # Converting 'numpy.float32' datatype into 'float'
                    similarity_score = (1.0 / (1.0 + dist)) * 100.0             # Percentage similarity score
                    similarity_score = round(similarity_score, 2)               # Rounding off the percentage decimal value (default=2)


                    self.db[const.table2_preferencesBasedMatchedProfiles].update_one(
                                                                            filter={'user_id': item['user_id'],
                                                                                    'preference_image_s3key': item['preference_image_s3key'],
                                                                                    },
                                                                            update={"$addToSet": {'matched_users':
                                                                                                  {'match_user_id': push_profile_table2["user_id"],
                                                                                                   'match_gender': push_profile_table2["gender"],
                                                                                                   'match_img_s3key': push_profile_table2['profile_image_s3key'],
                                                                                                   'match_percentage': similarity_score,
                                                                                                   'match_dist': dist,
                                                                                                   }
                                                                                              }
                                                                                    },
                                                                            upsert=True)
            #
            # # self.db[const.table2_preferencesBasedMatchedProfiles].replace_one(filter={'user_id': record_for_table2['user_id'],
            # #                                                                    'preference_media_url_objKey': record_for_table2['preference_media_url_objKey'],
            # #                                                                     },
            # #
            # #
            # #                                                                update={"$set": {'user_id': record_for_table2['user_id'],
            # #                                                                         'preference_media_url_objKey': record_for_table2['preference_media_url_objKey'],
            # #                                                                         'matched_users': record_for_table2['matched_users']
            # #                                                                          }
            # #                                                               },
            # #                                                               upsert=True)
            #
            return {"status": 1, "message": const.table2_preferencesBasedMatchedProfiles + " is pushed for each user "}

        except Exception as e:
            utils.logger.error("Exception occurred while inserting %age matched users into Table_2 : " + str(e))
            return {"status": -1, "message": const.table2_preferencesBasedMatchedProfiles + " is NOT updated"}





    # ------------------------------------------- Inserting Documents into table_2 -------------------------------------

    def insert_matched_users_with_percentage_table2(self, update_data_table2):
        '''
        Insert matched users list with percentage match along with other details into Table_2.
        In this table we have 'user_id' and 'preference_image_id' are primary key.
        '''
        try:
            update_data_table2['preference_image_embedding'] = Binary(pickle.dumps(update_data_table2['preference_image_embedding'], protocol=2), subtype=128)

            self.db[const.table2_preferencesBasedMatchedProfiles].update_one(filter={'user_id': update_data_table2['user_id'],
                                                                               'preference_image_s3key': update_data_table2['preference_image_s3key'],
                                                                                },
                                                                           update={"$set":
                                                                               {
                                                                                    'user_id': update_data_table2['user_id'],
                                                                                    'gender': update_data_table2['gender'],
                                                                                    'sexual_orientation': update_data_table2['sex_orientation'],
                                                                                    'preference_image_s3key': update_data_table2['preference_image_s3key'],
                                                                                    'preference_image_embedding': update_data_table2['preference_image_embedding'],
                                                                                    'matched_users': update_data_table2['matched_users']
                                                                                }
                                                                          },
                                                                          upsert=True)


            return {"status": 1, "message": const.table2_preferencesBasedMatchedProfiles + " is updated"}

        except Exception as e:
            utils.logger.error("Exception occurred while inserting %age matched users into Table_2 : " + str(e))
            return {"status": -1, "message": const.table2_preferencesBasedMatchedProfiles + " is NOT updated"}










#***********************************************************************************************************************************************************************************************
#***********************************************************************************************************************************************************************************************
#***********************************************************************************************************************************************************************************************
#***********************************************************************************************************************************************************************************************
#***********************************************************************************************************************************************************************************************

    """                                                        
                                                            SEARCHING FROM MONGO DATABASE
    
    """

#------------------------------------------------- SEARCHING FROM MONGODB COLLECTIONS   --------------------------------------------------------------------------------------------------------------

    # ------------------------------------------- Searching profiles with right query from table_1 ---------------------
    def find_profileImageVector_from_table1(self, user_data_json):
        '''
        Searching profiles with right query from table_1
        :param user_data_json:
        :return: profile_image_embeddings_list
        '''
        mongo_query_table1 = {
            'type': 'profile',
            'is_dp': True
        }

        if user_data_json["gender"] == 'Male':
            mongo_query_table1['gender'] = 'Female'

        elif user_data_json["gender"] == 'Female':
            mongo_query_table1['gender'] = 'Male'
            
        else:
            utils.logger.error("Query is not formatted because 'user_gender' is not entered--")
            return "Please enter correct information"


        profiles_list_from_mongodb = list(self.db[const.table1_profileVectorizedImages].find(mongo_query_table1))
        profile_image_embeddings_list = []

        for i in profiles_list_from_mongodb:
            # print(i.keys())
            i['profile_image_embedding'] = pickle.loads(i['profile_image_embedding'])
            profile_image_embeddings_list.append(i)

        return profile_image_embeddings_list



    # ------------------------------------------- Searching users with uploaded preference images from table_2 ---------

    def find_preferenceImageVector_from_table2(self, user_data_json):
        '''
        Searching All preference image_vectors from table_2 to push new profile image matching into matched_users (array) into table2.
        :param user_data_json:
        :return: list of image_vectors
        '''

        mongo_query_table2 = {
            'preference_gender': user_data_json["preference_gender"]
        }

        preference_list_from_mongodb = list(self.db[const.table2_preferencesBasedMatchedProfiles].find(mongo_query_table2))
        preference_image_embeddings_list = []

        for i in preference_list_from_mongodb:
            # print(i.keys())
            i['preference_image_embedding'] = pickle.loads(i['preference_image_embedding'])
            preference_image_embeddings_list.append(i)

        return preference_image_embeddings_list


    # ------------------------------------------- Searching matched users from table_2 ---------------------------------
    def find_matched_users_from_table2(self, user_id, match_percentage, preference_image_s3key):
        '''
        Searching matched users from table_2
        :param user_id:
        :param match_percentage:
        :param preference_image_s3key:
        :return:
        '''
        result = []
        matched_users_list = list(self.db[const.table2_preferencesBasedMatchedProfiles].find({"user_id": user_id, "preference_image_s3key": preference_image_s3key}))

        if len(matched_users_list) == 0:
            pass
        else:
            for i in matched_users_list:
                for j in i["matched_users"]:
                    if j["match_percentage"] >= match_percentage:
                        result.append(j)

            result = sorted(result, key=lambda k: k["match_percentage"], reverse=True)

        return result


    def find_default_users_from_table2(self, user_id, match_percentage):
        '''
        Searching matched users from table_2 when
        :param user_id:
        :param match_percentage:
        :param preference_image_s3key:
        :return:
        '''
        result = []
        matched_users_list = list(self.db[const.table2_preferencesBasedMatchedProfiles].find( {"user_id": user_id} ))

        if len(matched_users_list) == 0:
            pass
        else:
            for i in matched_users_list:
                for j in i["matched_users"]:
                    if j["match_percentage"] >= match_percentage:
                        result.append(j)

            result = sorted(result, key=lambda k: k["match_percentage"], reverse=True)

        return result


    # def find_matched_users2(self, user_id, match_percentage):
    #
    #     result = []
    #     matched_users_list = list(self.db[const.table2_preferencesBasedMatchedProfiles].find({}))
    #
    #     for i in matched_users_list:
    #         if i['user_id'] == user_id:
    #            matched_users_list = i['matched_users']
    #
    #
    #     for i in matched_users_list:
    #         if i["match_percentage"] >= match_percentage:
    #                 result.append(i)
    #
    #     result = sorted(result, key=lambda k: k["match_percentage"], reverse=True)
    #
    #     return result




# -------------------------------------------------  MONGODB SEARCH FOR RECOMMENDATIONS------------------------------------------------

    # ------------------------------------------- Searching profile with given 'user_id' from the 'users' collection. ---------------------

    def find_user_data(self, user_id):
        '''
        Searching user's data with given 'user_id' from the 'users' collection.
        :param user_id:
        :return: user's details
        '''

        try:
            user_data = list(self.db['users'].find({"user_id" : user_id}))

            return user_data[0]

        except Exception as e:
            utils.logger.exception("__Error while searching user details from 'user' collection in MongoDB__" + str(e))


    # ------------------------------------------- Searching profiles with right query from table_1 ---------------------
    def find_profiles_having_similar_interests_spoken_languages(self, user_data):
        '''
        Searching profile with given user_id from the 'users' collection.
        :param user_data:
        :return: profile details
        '''

        # if user_data["aInterest"] == ['']:
        #     user_interests_list = user_data["aInterest"]
        # else:
        #     user_interests_list = [x["interest"] for x in user_data["aInterest"]]
        #
        # if user_data["aLanguage"] == ['']:
        #     user_languages_list = user_data["aLanguage"]
        # else:
        #     user_languages_list = [x["language"] for x in user_data["aLanguage"]]


        user_interests_list = ""
        user_languages_list = ""

        if "aInterest" in user_data.keys():
            user_interests_list = [x for x in user_data["aInterest"]]

        if "aLanguage" in user_data.keys():
            user_languages_list = [x for x in user_data["aLanguage"]]



        # user_coordinates = [x for x in user_data["geometry"]["coordinates"]]


        try:
            # db["mydb"].find(
            #     {"$and": [
            #         {"field": var1},
            #         {"field": {
            #             "$ne": var2
            #         }}
            #     ]}
            # )


            # ll = list(self.db["users"].find(
            #     {"$and": [
            #             {"user_id": {"$ne": user_data["user_id"]}},
            #             {"gender": user_data["gender"]}
            #         ]
            #     }
            #     ))


            similar_interests_users_list = list(self.db['users'].find(
                                        {"$and":
                                            [
                                                {"$and":
                                                [
                                                    {"user_id": {"$ne": user_data["user_id"]}},
                                                    {"gender": user_data["gender"]}
                                                ]
                                                },

                                                {
                                                 "$or":
                                                    [
                                                        {"aInterest":
                                                            {"$elemMatch":  {"$in": user_interests_list}}
                                                         },
                                                        {"aLanguage":
                                                            {"$elemMatch": {"$in": user_languages_list}}
                                                         },
                                                        {
                                                            "body_type": user_data["body_type"]
                                                        },
                                                        {
                                                            "profession": user_data["profession"]
                                                        },
                                                        {
                                                            "sex_orientation": user_data["sex_orientation"]
                                                        },
                                                        {
                                                            "location": user_data["location"]
                                                        },

                                                    ]
                                                }
                                            ]
                                        }
                                    )
                                )

            pprint(similar_interests_users_list)
            return similar_interests_users_list

        except Exception as e:
            utils.logger.exception("__Error while searching user details from 'user' collection in MongoDB__" + str(e))





    # -------------------------------------------Finding recommended profiles to be displayed on discovery page for a user ---------------------
    def mongodb_search_to_recommend_profiles_for_discovery_page(self, user_data):
        '''
        Searching profile with given user_id from the 'users' collection.
        :param user_data:
        :return: profile details
        '''

        user_interests_list = ""
        user_languages_list = ""

        if "aInterest" in user_data.keys():
            user_interests_list = [x for x in user_data["aInterest"]]

        if "aLanguage" in user_data.keys():
            user_languages_list = [x for x in user_data["aLanguage"]]


        # user_coordinates = [x for x in user_data["geometry"]["coordinates"]]


        try:
            # db["mydb"].find(
            #     {"$and": [
            #         {"field": var1},
            #         {"field": {
            #             "$ne": var2
            #         }}
            #     ]}
            # )

            gender = ''
            if user_data["gender"] == "Male":
                gender = "Female"
            elif user_data["gender"] == "Female":
                gender = "Male"


            # ll = list(self.db["users"].find(
            #     {"$and": [
            #             {"user_id": {"$ne": user_data["user_id"]}},
            #             {"gender": gender}
            #         ]
            #     }
            #     ))


            # similar_interests_but_opposite_gender_users_list = list(self.db['users'].find(
            #             {"$and":
            #                 [
            #                     {"$and":
            #                         [
            #                             {"user_id": {"$ne": user_data["user_id"]}},
            #                             {"gender": gender}
            #                         ]
            #                     },
            #
            #                     {
            #                      "$or":
            #                         [
            #                             {"aInterest":
            #                                 {"$elemMatch": {"interest": {"$in": user_interests_list}}}
            #                              },
            #                             {"aLanguage":
            #                                 {"$elemMatch": {"language": {"$in": user_languages_list}}}
            #                              },
            #                         ]
            #                     }
            #                 ]
            #             }
            #         )
            #     )


            similar_interests_but_opposite_gender_users_list = list(self.db['users'].find(
                        {"$and":
                            [
                                {"$and":
                                    [
                                        {"user_id": {"$ne": user_data["user_id"]}},
                                        {"gender": gender},
                                        # {"sex_orientation": user_data["sex_orientation"]}
                                    ]
                                },

                                {
                                    "$or":
                                        [
                                            {"aInterest":
                                                 {"$elemMatch": {"$in": user_interests_list}}
                                             },
                                            {"aLanguage":
                                                 {"$elemMatch": {"$in": user_languages_list}}
                                             },
                                            {
                                                "body_type": user_data["body_type"]
                                            },
                                            {
                                                "profession": user_data["profession"]
                                            },
                                            {
                                                "sex_orientation": user_data["sex_orientation"]
                                            },
                                            {
                                                "location": user_data["location"]
                                            },

                                        ]
                                    }
                                ]
                            }
                        )
                    )

            pprint(similar_interests_but_opposite_gender_users_list)
            return similar_interests_but_opposite_gender_users_list

        except Exception as e:
            utils.logger.exception("__Error while searching user details from 'user' collection in MongoDB__" + str(e))




    # ------------------------------------------- Searching profile with given user_id from the 'friend_statuses' collection. ---------------------

    def discover_new_friends(self, user_id):
        '''
        Finding those profiles who have not yet discovered by the users.
        The use has taken some actions against other profile. Requirement is to find those users who are not yet discovered.
        :param user_data:
        :return: profile details
        '''

        try:
            # mongo_query_interest = {
            #     'account_type': 'exfactor',
            #     'interest': interest,
            #
            # }
            lst_friends_statuses = list(self.db["friend_statuses"].find({"from_user_id": user_id}))

            discovered_friends = []

            for i in lst_friends_statuses:
                discovered_friends.append(i["to_user_id"])


            return discovered_friends

        except Exception as e:
            utils.logger.exception("__Error while searching user details from 'user' collection in MongoDB__" + str(e))
