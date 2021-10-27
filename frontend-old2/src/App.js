import react from 'react'
import { Route, Redirect, Switch } from 'react-router';
import { Navigation, Home } from 'common';
import { BackTracking, BruteForce, DivideConquer, DynamicProgramming, Greedy } from 'features/algorithm'
import { Linearity, Nonlinear, Math } from 'features/datastructure';
import { SignUp } from 'features/user'
import { CounterOld } from 'features/counterOld'
import { Todo } from 'features/todos'
import { createStore, combineReducers } from 'redux'
import { Provider } from 'react-redux' //데이터 베이스와 연결해주는 역할(ex: MyBatis)
import { store } from 'app/store'

const App = () =>(
    <Provider store={store}>
      <Navigation/>
      <Switch>
        <Route exact path='/' component= {Home}/>
        <Redirect from='/Home' to ={'/'}/>
        <Route exact path='/CounterOld' component={CounterOld}/>
        <Route exact path='/Todo' component={Todo}/>
        <Route exact path='/SignUp' component={SignUp}/>
        <Route exact path='/Back-tracking' component={BackTracking}/>
        <Route exact path='/Brute-force' component={BruteForce}/>
        <Route exact path='/Divide-conquer' component={DivideConquer}/>
        <Route exact path='/Dynamic-programming' component={DynamicProgramming}/>
        <Route exact path='/Greedy' component={Greedy}/>
        <Route exact path='/Greedy' component={Math}/>
        <Route exact path='/Linearity' component={Linearity}/>
        <Route exact path='/Nonlinear' component={Nonlinear}/>
      </Switch>
    </Provider>
)

export default App;