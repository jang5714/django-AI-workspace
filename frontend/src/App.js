import react from 'react'
import { Route, Redirect, Switch } from 'react-router';
import {Navigation, Home, Counter, Todo} from 'common';
import { BackTracking, BruteForce, DivideConquer, DynamicProgramming, Greedy } from 'algorithm';
import { Linearity, Math, Nonlinear } from 'datastructure';

const App = () =>(
  <>
  <Navigation/>
  <Switch>
    <Route exact path='/' component= {Home}/>
    
    <Redirect from='/Home' to ={'/'}/>
    <Route exact path='/Counter' component={Counter}/>
    <Route exact path='/Todo' component={Todo}/>
    <Route exact path='/BackTracking' component={BackTracking}/>
    <Route exact path='/BruteForce' component={BruteForce}/>
    <Route exact path='/DivideConquer' component={DivideConquer}/>
    <Route exact path='/DynamicProgramming' component={DynamicProgramming}/>
    <Route exact path='/Greedy' component={Greedy}/>
    <Route exact path='/Linearity' component={Linearity}/>
    <Route exact path='/Math' component={Math}/>
    <Route exact path='/Nonlinear' component={Nonlinear}/>
  </Switch>
  </>
)

export default App;
