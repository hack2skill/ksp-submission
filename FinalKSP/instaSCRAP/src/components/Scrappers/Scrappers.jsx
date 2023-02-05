import React,{useEffect} from "react";
import { Link, useNavigate } from "react-router-dom";
import "./Scrapper.css";

export default function Scappers() {
	const navigate = useNavigate()
	useEffect(() =>{
		if(sessionStorage.getItem("token") == null || sessionStorage.getItem("token") == null|| sessionStorage.getItem("token").length<9  ){
			navigate('/login')
		}
	},[])
  return (
    <div className="bg-[#FEFEFF] h-full mx-auto w-full xs:w-full sm:w-full md:w-3/4 lg:w-4/5 xl:w-4/5 flex flex-col pt-9">
			<div className="flex flex-row w-full">
				<div className="flex flex-col items-start">
					<h2 className="mb-2 text-2xl font-semibold">ScrapperOP</h2>
					<p className="text-muted-dark-gray">
						Get rich analysis for any public account.
					</p>
				</div>
			</div>

			<div className="flex flex-row flex-wrap items-center gap-5 mb-7 mt-7 xs:flex-wrap sm:flex-wrap md:flex-wrap lg:flex-nowrap xl:flex-nowrap">

      <Link
					to="/scrape/phone"
					className="w-full xs:w-full sm:w-full md:w-full lg:w-1/2 xl:w-1/2 flex flex-row items-center gap-8 px-6 h-[217px] border border-gray-200 shadow-md hover:shadow-lg transition-all rounded-xl hover:border-purpl/50 hover:bg-purpl/10 shadow-gray-300/30"
				>
					<img
						src="https://i.postimg.cc/QMmtCw4r/telepon-7745.png"
						className="w-[80px] xs:w-[80px] sm:w-[80px] md:w-[100px] lg:w-[120px] xl:w-[120px] 2xl:w-[150px] h-auto"
					/>
					<div className="flex flex-col items-start gap-4">
						<h3 className="text-xl font-semibold">Phone Number Scrapper</h3>
						<p className="text-sm font-medium text-gray-500">
						Effortlessly gather accurate phone numbers with a user-friendly scrapper that streamlines the data extraction process for maximum efficiency
						</p>
					</div>
				</Link>

        <Link
					to="/scrape/twitter"
					className="w-full xs:w-full sm:w-full md:w-full lg:w-1/2 xl:w-1/2 flex flex-row items-center gap-8 px-6 h-[217px] border border-gray-200 shadow-md hover:shadow-lg transition-all rounded-xl hover:border-purpl/50 hover:bg-purpl/10 shadow-gray-300/30"
				>
					<img
						src="https://i.postimg.cc/Qdgmk4Zd/logo-twitter-png-5860.png"
						className="w-[80px] xs:w-[80px] sm:w-[80px] md:w-[100px] lg:w-[120px] xl:w-[120px] 2xl:w-[150px] h-auto"
					/>
					<div className="flex flex-col items-start gap-4">
						<h3 className="text-xl font-semibold">Twitter Scrapper</h3>
						<p className="text-sm font-medium text-gray-500">
            Easily gather insights and information from Twitter with a user-friendly scrapper that simplifies the data extraction process.
						</p>
					</div>
				</Link>

				
			</div>

			{/* <div className="flex flex-row w-full">
				<div className="flex flex-col items-start">
					<h2 className="mb-2 text-2xl font-semibold">Sector Analysis</h2>
					<p className="text-muted-dark-gray">
						Generate fact-based market research reports for any topic
					</p>
				</div>
			</div> */}



			<div className="flex flex-row flex-wrap items-center gap-5 mt-7 xs:flex-wrap sm:flex-wrap md:flex-wrap lg:flex-nowrap xl:flex-nowrap">

      

        <Link
					to="/scrape/linkedin"
					className="relative w-full xs:w-full sm:w-full md:w-full lg:w-1/2 xl:w-1/2 flex flex-row items-center gap-8 px-6 h-[217px] border border-gray-200 shadow-md hover:shadow-lg transition-all rounded-xl shadow-gray-300/30 hover:border-purpl/50 hover:bg-purpl/10"
				>
					<img
						src="https://i.postimg.cc/Y0bGCW5k/linkedin-logo-png-1825.png"
						className="w-[80px] xs:w-[80px] sm:w-[80px] md:w-[100px] lg:w-[120px] xl:w-[120px] 2xl:w-[150px] h-auto"
					/>
					<div className="flex flex-col items-start gap-4">
						<h3 className="text-xl font-semibold">LinkedIn Scrapper</h3>
						<p className="text-sm font-medium text-gray-500">
            Empower your investigations with the power of professional networking – our LinkedIn Scraper provides law enforcement with quick and easy access to crucial information on individuals.
						</p>
					</div>
				</Link>

				<Link
					to="/scrape/facebook"
					className="w-full xs:w-full sm:w-full md:w-full lg:w-1/2 xl:w-1/2 flex flex-row items-center gap-8 px-6 h-[217px] border border-gray-200 shadow-md hover:shadow-lg transition-all rounded-xl shadow-gray-300/30 hover:border-purpl/50 hover:bg-purpl/10"
				>
					<img
						src="https://i.postimg.cc/htSj8CRP/facebook-logo-481.png"
						className="w-[80px] xs:w-[80px] sm:w-[80px] md:w-[100px] lg:w-[120px] xl:w-[120px] 2xl:w-[150px] h-auto"
					/>
					<div className="flex flex-col items-start gap-4">
						<h3 className="text-xl font-semibold">Facebook Scrapper</h3>
						<p className="text-sm font-medium text-gray-500">
            Unlock a wealth of information with the click of a button using our Facebook Scraper – the must-have tool for law enforcement looking to quickly gather intelligence on individuals.
						</p>
					</div>
				</Link>

				
        
			</div>
      <div className="flex flex-row flex-wrap items-center gap-5 mt-7 xs:flex-wrap sm:flex-wrap md:flex-wrap lg:flex-nowrap xl:flex-nowrap">
      

      <Link
					to="/scrape/instagram"
					className="w-full xs:w-full sm:w-full md:w-full lg:w-1/2 xl:w-1/2 flex flex-row items-center gap-8 px-6 h-[217px] border border-gray-200 shadow-md hover:shadow-lg transition-all rounded-xl shadow-gray-300/30 hover:border-purpl/50 hover:bg-purpl/10"
				>
					<img
						src="https://i.postimg.cc/G3MZvpJ5/logo-ig-png-32464.png"
						className="w-[80px] xs:w-[80px] sm:w-[80px] md:w-[100px] lg:w-[120px] xl:w-[120px] 2xl:w-[150px] h-auto"
					/>
					<div className="flex flex-col items-start gap-4">
						<h3 className="text-xl font-semibold">Instagram Scrapper</h3>
						<p className="text-sm font-medium text-gray-500">
            Effortlessly gather valuable insights from Instagram with a user-friendly scrapper that makes data extraction a breeze.
						</p>
					</div>
				</Link>
  
        </div>
		</div>
  )
}
