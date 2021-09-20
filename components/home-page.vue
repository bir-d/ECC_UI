<template>
  <div class="overall">
    <div class="columns">
      <div class="column">
        <a href="/videowall">
          <figure class="image is-16by9">
            <img src="../assets/home-video-wall.png">
          </figure>
          <div class="content" id="title-label">
            <h4>Video Wall</h4>
          </div>
        </a>
      </div>
      <div class="column">
        <a href="#">
          <figure class="image is-16by9">
            <img src="../assets/home-workstation.png">
          </figure>
          <div class="content" id="title-label">
            <h4>Workstations</h4>
          </div>
        </a>
      </div>
      <div class="column">
        <a href="/lights">
          <figure class="image is-16by9">
            <img src="../assets/home-lights.png">
          </figure>
          <div class="content" id="title-label">
            <h4>Lights</h4>
          </div>
        </a>
      </div>
      <div class="column">
<!--        this is the router-link to the display pages from homepages-->
        <a href="/display">
          <figure class="image is-16by9">
            <img src="../assets/home-displays.png">
          </figure>
          <div class="content" id="title-label">
            <h4>Displays</h4>
          </div>
        </a>
      </div>
    </div>
    <hr>
    <div class="recents">
      <div class="content">
        <h2 class="is-size-3 is-underlined has-text-left">Recently Used</h2>
      </div>
      <div class="columns" id="recent-section">
        <div class="column is-2">
            <div class="level-item has-text-centered">
              <a>
                <figure class="image is-128x128">
                  <img id="recent-image" class="is-rounded" src="https://bulma.io/images/placeholders/128x128.png">
                </figure>
                <div class="content has-text-centered is-size-5" id="title-label">
                  <p>Preset</p>
                </div>
              </a>
            </div>
          </div>
          <div class="column is-2">
            <div class="level-item has-text-centered">
              <a>
                <figure class="image is-128x128">
                  <img id="recent-image" class="is-rounded" src="https://bulma.io/images/placeholders/128x128.png">
                </figure>
                <div class="content has-text-centered is-size-5" id="title-label">
                  <p>Preset</p>
                </div>
              </a>
            </div>
          </div>
          <div class="column is-2">
            <div class="level-item has-text-centered">
              <a>
                <figure class="image is-128x128">
                  <img id="recent-image" class="is-rounded" src="https://bulma.io/images/placeholders/128x128.png">
                </figure>
                <div class="content has-text-centered is-size-5" id="title-label">
                  <p>Preset</p>
                </div>
              </a>
            </div>
          </div>
          <div class="column is-2">
           <div class="level-item has-text-centered">
              <a>
                <figure class="image is-128x128">
                  <img id="recent-image" class="is-rounded" src="https://bulma.io/images/placeholders/128x128.png">
                </figure>
                <div class="content has-text-centered is-size-5" id="title-label">
                  <p>Preset</p>
                </div>
              </a>
            </div>
          </div>
          <div class="column is-2">
            <div class="level-item has-text-centered">
              <a>
                <figure class="image is-128x128">
                  <img id="recent-image" class="is-rounded" src="https://bulma.io/images/placeholders/128x128.png">
                </figure>
                <div class="content has-text-centered is-size-5" id="title-label">
                  <p>Preset</p>
                </div>
              </a>
            </div>
          </div>
          <div class="column is-2">
            <div class="level-item has-text-centered">
              <a>
                <figure class="image is-128x128">
                  <img id="recent-image" class="is-rounded" src="https://bulma.io/images/placeholders/128x128.png">
                </figure>
                <div class="content has-text-centered is-size-5" id="title-label">
                  <p>Preset</p>
                </div>
              </a>
            </div>
          </div>
        </div>
    </div>
  </div>
</template>

<style scoped>
.overall{
  margin-top: 6em;
  margin-bottom: 4em;
  margin-left: 3em;
  margin-right: 3em;
}
#recent-section{
  margin-left: 2em;
  margin-top: 2em;
}
#title-label{
  margin-top: 2em;
  font-family: monospace;
}
figure{
  transition: all 0.2s ease;
  transition-property: transform, opacity, color, border-color, background-color;
}
figure:hover{
  transform: scale(1.05);
}
</style>