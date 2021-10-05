import * as React from 'react';
import Avatar from '@mui/material/Avatar';
import Button from '@mui/material/Button';
import CssBaseline from '@mui/material/CssBaseline';
import TextField from '@mui/material/TextField';
import FormControlLabel from '@mui/material/FormControlLabel';
import Checkbox from '@mui/material/Checkbox';
import Link from '@mui/material/Link';
import Grid from '@mui/material/Grid';
import Box from '@mui/material/Box';
import LockOutlinedIcon from '@mui/icons-material/LockOutlined';
import Typography from '@mui/material/Typography';
import Container from '@mui/material/Container';
import { createTheme, ThemeProvider } from '@mui/material/styles';
import { useState } from 'react'
import { useDispatch } from 'react-redux';
import { addUserAction } from 'features/user/modules/userSlice';
import { userRegister} from 'features/user/modules/userAPI'

function Copyright(props) {
  return (
    <Typography variant="body2" color="text.secondary" align="center" {...props}>
      {'Copyright © '}
      <Link color="inherit" href="https://material-ui.com/">
        Your Website
      </Link>{' '}
      {new Date().getFullYear()}
      {'.'}
    </Typography>
  );
}

const theme = createTheme();

export default function UserJoin() {
  const [user, setUser] = useState({
          username: '',
          name: '',
          birth: '',
          address: '',
          email: '',
          password: '',
        })
  const {username, password, name, email, birth, address} = `user`
  
  const handleSubmit = e => {
      e.preventDefault();
      alert(`가입 회원정보 : ${JSON.stringify(user)}`)// 스트링으로 변화게 하다 안하면 인간이 못알아 보게 된다.
      userRegister({user}) //DB 저장 
      .then(res => {alert(`회원가입완료: ${res.data.result}`)})
      .catch(err => {alert(`회원가입 실패 : ${err}`)})
    }
  
  const handleChange = e => {
      e.preventDefault() // 바로 이벤트가 즉시 실행되지 못하게 하기 위해 작성 필수
      const {name, value} = e.target
      // alert(`name: ${name}, value: ${value}`)
      setUser({
        ...user,
        [name]: value
      })
  }

  return (
    <ThemeProvider theme={theme}>
      <Container component="main" maxWidth="xs">
        <CssBaseline />
        <Box
          sx={{
            marginTop: 8,
            display: 'flex',
            flexDirection: 'column',
            alignItems: 'center',
          }}
        >
          <Avatar sx={{ m: 1, bgcolor: 'secondary.main' }}>
            <LockOutlinedIcon />
          </Avatar>
          <Typography component="h1" variant="h5">
            Sign Up
          </Typography>
          <Box component="form" onSubmit={handleSubmit} noValidate sx={{ mt: 1 }}>
          <TextField onChange = {handleChange}
              margin="normal"
              required
              fullWidth
              name="username"
              label="username"
              type="text"
              id="username"
              value = {username}
              autoComplete="current-username"
            />
            <TextField onChange = {handleChange}
              margin="normal"
              required
              fullWidth
              id="email"
              label="Email Address"
              name="email"
              type="email"
              value = {email}
              autoComplete="email"
              autoFocus
            />
            <TextField onChange = {handleChange}
              margin="normal"
              required
              fullWidth
              id="name"
              label="name"
              name="name"
              type="text"
              value = {name}
              autoComplete="name"
              autoFocus
            />
            <TextField onChange = {handleChange}
              margin="normal"
              required
              fullWidth
              name="password"
              label="password"
              type="password"
              id="password"
              value = {password}
              autoComplete="current-password"
            />            
            <TextField onChange = {handleChange}
              margin="normal"
              required
              fullWidth
              name="address"
              label="address"
              type="text"
              id="address"
              value = {address}
              autoComplete="current-address"
            />
            <TextField onChange = {handleChange}
              margin="normal"
              required
              fullWidth
              name="birth"
              label="birth"
              type="text"
              id="birth"
              value = {birth}
              autoComplete="current-birth"
            />

            <FormControlLabel
              control={<Checkbox value="remember" color="primary" />}
              label="Remember me"
            />
            <Button
              type="submit"
              fullWidth
              variant="contained"
              sx={{ mt: 3, mb: 2 }}
            >
              Sign In
            </Button>
            <Button
              type="button"
              fullWidth
              variant="contained"
              sx={{ mt: 3, mb: 2 }}
            >
              Cancel
            </Button>
          </Box>
        </Box>
        <Copyright sx={{ mt: 8, mb: 4 }} />
      </Container>
    </ThemeProvider>
  );
}