
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>PyTerminal Web - {{title}}</title>

  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="Python terminal in web browser">
  <meta name="author" content="Marc CARRE">

  <link href="//netdna.bootstrapcdn.com/bootswatch/2.3.1/cyborg/bootstrap.min.css" rel="stylesheet" />
  <link href="//twitter.github.io/bootstrap/assets/js/google-code-prettify/prettify.css" rel="stylesheet" />

  <script src="//ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js"></script>
  <script src="//netdna.bootstrapcdn.com/twitter-bootstrap/2.3.1/js/bootstrap.min.js"></script>
  <script src="//twitter.github.io/bootstrap/assets/js/google-code-prettify/prettify.js"></script>
  <style>
    body {
      padding-top: 60px; /* 60px to make the container go all the way to the bottom of the topbar */
    }
    .prompt {
      color: white;
    }
  </style>
</head>
<body>
    <div class="navbar navbar-inverse navbar-fixed-top">
      <div class="navbar-inner">
        <div class="container">
          <a class="brand" href="#">PyTerminal Web</a>
          <div class="nav-collapse collapse">
            <ul class="nav">
% if title == 'Terminal':
              <li class="active"><a href="/">Home</a></li>
              <li><a href="/sources">Source code</a></li>
% else:
              <li><a href="/">Home</a></li>
              <li class="active"><a href="/sources">Source code</a></li>
% end
              <li><a href="" target="_blank">GitHub</a></li>
            </ul>
          </div><!--/.nav-collapse -->
        </div>
      </div>
    </div>

    <div class="container">