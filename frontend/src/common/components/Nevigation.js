import react from 'react' 
import styled from 'styled-components'
import { Link } from 'react-router-dom'

const Navigation = () => (
    <>
    <Nav class="navi" color="white">
        <NavItem>
            <NavList><Link to="/Counter">Counter</Link></NavList> 
            <NavList><Link to="/Todo">Todo</Link></NavList>
            <NavList><Link to="/Signup">Signup</Link></NavList>
            <NavList><Link to="/Math">Math</Link></NavList>
            <NavList><Link to="/Linearity">Linearity</Link></NavList>
            <NavList><Link to="/Nonlinear">Nonlinear</Link></NavList>
            <NavList><Link to="/BruteForce">BruteForce</Link></NavList>
            <NavList><Link to="/DivideConquer">DivideConquer</Link></NavList>
            <NavList><Link to="/Greedy">Greedy</Link></NavList>
            <NavList><Link to="/DynamicProgramming">DynamicProgramming</Link></NavList>
            <NavList><Link to="/BackTracking">BackTracking</Link></NavList>
        </NavItem>
    </Nav>
    </>
)

export default Navigation

const Nav = styled.div`
    width: 100%;
    height: 30px;
    border-bottom: 1px solid #d1d8e4;
    color: white;
    z-index: 5;
    margin-bottom: 100px
`

const NavList = styled.ul`
    width: 1080px;
    display: flex;
    margin: 0 auto;
    color: white;
`

const NavItem = styled.li`
    width: auto;
    margin-left: 18px;
    margin-top: 5px;
    display: flex;
    color: white;
`