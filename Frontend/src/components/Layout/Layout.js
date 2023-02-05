import React from "react";
import {
  Route,
  Switch,
  Redirect,
  withRouter,
} from "react-router-dom";
import classnames from "classnames";

// styles
import useStyles from "./styles";

// components
import Header from "../Header";
import Sidebar from "../Sidebar";

// context
import { useLayoutState } from "../../context/LayoutContext";
import Dashboard from '../../pages/dashboard/Dashboard';

function Layout(props) {
  var classes = useStyles();

  // global
  var layoutState = useLayoutState();

  return (
    <div className={classes.root}>
        <>
          <Header history={props.history} />
          <Sidebar />
          <div
            className={classnames(classes.content, {
              [classes.contentShift]: layoutState.isSidebarOpened,
            })}
          >
            <div className={classes.fakeToolbar} />
            <Switch>
            <Route path="/app/dashboard" component={Dashboard} />
              <Route path="/app/items" render={() => <Redirect to="/app/dashboard" />} />
              <Route path="/app/edit" render={() => <Redirect to="/app/dashboard" />} />
              <Route path="/app/orders" render={() => <Redirect to="/app/dashboard" />} />
              <Route path="/app/notifications" render={() => <Redirect to="/app/dashboard" />} />  
              <Route
                exact
                path="/app/ui"
                render={() => <Redirect to="/app/dashboard" />}
              />
              <Route
                exact
                path="/app/dashboard/*"
                render={() => <Redirect to="/app/dashboard" />}
              />
              <Route path="/app/ui/maps" render={() => <Redirect to="/app/dashboard" />} />
              <Route path="/app/ui/icons" render={() => <Redirect to="/app/dashboard" />} />
              <Route path="/app/ui/charts" render={() => <Redirect to="/app/dashboard" />} />
            </Switch>
          </div>
        </>
    </div>
  );
}

export default withRouter(Layout);
