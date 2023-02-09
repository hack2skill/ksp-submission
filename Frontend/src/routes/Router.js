import React from 'react'
import { Route, Routes } from 'react-router-dom'
import Home from '../pages/Home/Home';
import Dashboard from '../pages/Dashboard/Dashboard';
import Missing from '../pages/Missing_Person/missing';
import Thief from '../pages/Theif/thief';
import { ROUTES } from './Routerconfig';
import Output from '../Components/outputimages/output';
import ThiefOutput from '../pages/ThiefOutput/thiefoutput';
import Lost_person from '../pages/Lost_Person/lost_person';
import AugOutput from '../pages/augoutput';
import LostOutput from '../pages/Lost_Output/lost_output';
import Augment from '../pages/augmentation/augmentation';
const Router = () => {

    const RouteWithRole = ({ Element }) => {
        return (
          <>
            <Element/>
          </>
        );
      }

  return (
    <div>
        <Routes>
            <Route exact path={ROUTES.Home} element={<RouteWithRole Element={Home} />}></Route>
            <Route exact path={ROUTES.Dashboard} element={<RouteWithRole Element={Dashboard} />}></Route>
            <Route exact path={ROUTES.Missing} element={<RouteWithRole Element={Missing} />}></Route>
            <Route exact path={ROUTES.Thief} element={<RouteWithRole Element={Thief} />}></Route>
            <Route exact path={ROUTES.Output} element={<RouteWithRole Element={Output}/>}></Route>
            <Route exact path={ROUTES.Thiefoutput} element={<RouteWithRole Element={ThiefOutput}/>}></Route>
            <Route exact path={ROUTES.LostPerson} element={<RouteWithRole Element={Lost_person}/>}></Route>
            <Route exact path={ROUTES.Lostoutput} element={<RouteWithRole Element={LostOutput}/>}></Route>
            <Route exact path={ROUTES.Augmentation} element={<RouteWithRole Element={Augment}/>}></Route>
            <Route exact path={ROUTES.Augoutput} element={<RouteWithRole Element={AugOutput}/>}></Route>
        </Routes>
    </div>
  )
}

export default Router