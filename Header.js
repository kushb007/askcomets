import React, { useEffect, useState} from 'react';
import { makeStyles } from '@material-ui/core/styles';
import { AppBar, Collapse, IconButton, Toolbar, Button} from '@material-ui/core';
import SortIcon from '@material-ui/icons/Sort';
import { Link } from 'react-router-dom';
//import ExpandMoreIcon from '@mui/icons-material/ExpandMore';

const useStyles = makeStyles((theme) => ({
  root: {
    display: 'flex',
    justifyContent: 'center',
    alignItems: 'center',
    height: '100vh',
    fontFamily: 'Nunito',
  },
  appbar: {
    background: '#0E6655BF',
  },
  appbarWrapper: {
    width: '80%',
    margin: '0 auto',
  },
  appbarTitle:{
    flexGrow: '1',
  },
  icon: {
    color: `#fff`,
    fontSize: '2rem',
  },
  colorText: {
    color: '#FF5733',
  },
  container:{
    textAlign: 'center',
  },
  title: {
    color: '#FFF',
    fontSize: '4.5rem',
  },
  title2: {
    color: '#FFF',
    fontSize: '4rem',
  },
  container2:{
    textAlign: 'center',
  },
  goDown:{
    textAlign: 'center',
    color: '#FF5733',
    fontSize: "4rem",
  },
}));
export default function Header() {
  const classes = useStyles();
  const [checked,setChecked] = useState(false);
  useEffect(() => {
    setChecked(true);
  },[])
  return (
  <div className={classes.root}>
    <AppBar className={classes.appbar} elevation={0}>
      <Toolbar className={classes.appbarWrapper}>
      <h1 className={classes.appbarTitle}><span className={classes.colorText}>Ask</span>Comets.</h1>
      <IconButton>
        <SortIcon className={classes.icon} />
      </IconButton>
      </Toolbar>
    </AppBar>
    <Collapse in={checked} 
    {...(checked ? { timeout: 1000 } : {})}
    collapsedHeight={50}>
    <div className={classes.container}>
      <h1 className={classes.title}>
        Welcome to <br /> <span className={classes.colorText}>Ask</span>Comets.
        <h1 className={classes.title2}>
        Your One Pit Stop <br /> For <span className={classes.colorText}>Comet</span> Help.
      </h1>
      </h1>
      </div>
      <div className={classes.container2}>
      <Button size ="large" variant="contained" href="/Forum">
  Click here to begin
</Button>
    </div>
    </Collapse>
  </div>)
  ;
}