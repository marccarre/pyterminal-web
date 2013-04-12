%include header title='Source code'
      <div class="row">
        <div class="tabbable">
          <ul class="nav nav-tabs">
            <li class="active"><a href="#python" data-toggle="tab">Python</a></li>
            <li><a href="#templates" data-toggle="tab">Templates</a></li>
          </ul>
          <div class="tab-content">
            <div class="tab-pane active" id="python">
              <pre class="prettyprint linenums">{{python}}</pre>
            </div>
            <div class="tab-pane" id="templates">
              <p><pre class="prettyprint linenums">{{header}}</pre></p>
              <p><pre class="prettyprint linenums">{{index}}</pre></p>
              <p><pre class="prettyprint linenums">{{sources}}</pre></p>
              <p><pre class="prettyprint linenums">{{footer}}</pre></p>
            </div>
          </div>
        </div>  
      </div>
      <script>
        !function ($) {
          $(function () {
            window.prettyPrint && prettyPrint()
          })
        }(window.jQuery)
      </script>
%include footer