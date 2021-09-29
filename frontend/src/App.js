import react from 'react'
import { Route, Redirect, Switch } from 'react-router';
import {Navigation, Home, Counter, Todo, SignUp} from 'common';
import { BackTracking, BruteForce, DivideConquer, DynamicProgramming, Greedy } from 'algorithm';
import { Linearity, Math, Nonlinear } from 'datastructure';
import { createStore, combineReducers } from 'redux'
import { Provider } from 'react-redux' //데이터 베이스와 연결해주는 역할(ex: MyBatis)
import { todoReducer, userReducer } from 'reducers'
const rootReducer = combineReducers({todoReducer, userReducer})
const store = createStore(rootReducer)


const App = () =>(
    <Provider store={store}>
      <Navigation/>
      <Switch>
        <Route exact path='/' component= {Home}/>
        <Redirect from='/Home' to ={'/'}/>
        <Route exact path='/Counter' component={Counter}/>
        <Route exact path='/Todo' component={Todo}/>
        <Route exact path='/SignUp' component={SignUp}/>
        <Route exact path='/BackTracking' component={BackTracking}/>
        <Route exact path='/BruteForce' component={BruteForce}/>
        <Route exact path='/DivideConquer' component={DivideConquer}/>
        <Route exact path='/DynamicProgramming' component={DynamicProgramming}/>
        <Route exact path='/Greedy' component={Greedy}/>
        <Route exact path='/Linearity' component={Linearity}/>
        <Route exact path='/Math' component={Math}/>
        <Route exact path='/Nonlinear' component={Nonlinear}/>
      </Switch>
    </Provider>
)

export default App;
