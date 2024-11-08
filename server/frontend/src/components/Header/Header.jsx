import React from 'react';
import "../assets/style.css"; 
import "../assets/bootstrap.min.css";

const Header = () => {
    // const [username, setUsername] = useState(null);

    // useEffect(() => {
    //     const storeUsername = sessionStorage.getItem("username");
    //     setUsername(storeUsername);
    // }, []);

    const logout = async (e) => {
    e.preventDefault();
    let logout_url = window.location.origin+"/djangoapp/logout";
    const res = await fetch(logout_url, {
      method: "GET",
    });
  
    const json = await res.json();
    if (json) {
      let username = sessionStorage.getItem('username');
    //   setUsername(null);
      sessionStorage.removeItem('username');
      window.location.href = window.location.origin;
      window.location.reload();
      alert("Logging out "+username+"...")
    }
    else {
      alert("The user could not be logged out.")
    }
  };
    
//The default home page items are the login details panel
let home_page_items =  <div></div>

//Gets the username in the current session
let curr_user = sessionStorage.getItem('username')

//If the user is logged in, show the username and logout option on home page
if ( curr_user !== null &&  curr_user !== "") {

// if (username) {
    home_page_items = (
    <div className="user-controls">
      <div className='username'>👋, {sessionStorage.getItem("username")}</div>
      {/* <div className='username'>👋, {username}</div> */}
      <a className="nav-link nav_item" href="/djangoapp/logout" onClick={logout}>Logout</a>
    </div>
    );
} else {
    home_page_items = (
        <a className="login_link nav-link" href="/login">Login</a>
    );
}

    return (
        <div className='navcontainer'>
          <nav class="navbar navbar-expand-lg">
            <div class="container-fluid">
              <h2 className="small_header">ZoomZoom</h2>
              <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarText" aria-controls="navbarText" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
              </button>
              <div class="collapse navbar-collapse" id="navbarText">
                <ul class="navbar-nav me-auto mb-2 mb-lg-0 navitems">
                  <li class="nav-item">
                    <a class="nav-link nav_item active" aria-current="page" href="/">Home</a>
                  </li>
                  <li class="nav-item">
                    <a class="nav-link nav_item" href="/about">About Us</a>
                  </li>
                  <li class="nav-item">
                    <a class="nav-link nav_item" href="/contact">Contact Us</a>
                  </li>
                </ul>
                <span class="navbar-text">
                  <div class="loginlink" id="loginlogout">
                    {home_page_items}
                  </div>
                  </span>
              </div>
            </div>
          </nav>
        </div>
    )
}

export default Header
