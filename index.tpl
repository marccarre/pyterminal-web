%include header title='Terminal'
      <div class="row output">
        %for entry in output:
          <div class="row">
            <div class="span12"><span class="prompt">&gt;&gt;&gt;&nbsp;</span>{{entry[0]}}<br />{{entry[1]}}</div>
          </div>
        %end
      </div>
      <div class="row">
        <form class="input-append" action="/" method="POST">
          <input class="input-xxlarge" id="txtCommand" name="command" type="text" />
          <input class="btn" type="submit" name="run" value="Run!" />
          <input class="btn" type="submit" name="reset" value="Reset" />
        </form>
      </div>
      <script>
        $(document).ready(function() {
          $('#txtCommand').focus();
        });
      </script>
%include footer
