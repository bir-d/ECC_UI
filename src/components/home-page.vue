<template>
  <div class="overall">
    <div class="columns">
      <div class="column">
        <a>
          <figure class="image is-16by9">
            <img src="../assets/home-video-wall.png">
          </figure>
        </a>
      </div>
      <div class="column">
        <a>
          <figure class="image is-16by9">
            <img src="../assets/home-workstation.png">
          </figure>
        </a>
      </div>
      <div class="column">
        <a>
          <figure class="image is-16by9">
            <img src="../assets/home-lights.png">
          </figure>
        </a>
      </div>
      <div class="column">
        <a>
          <figure class="image is-16by9">
            <img src="../assets/home-displays.png">
          </figure>
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
          <a>
            <figure class="image is-128x128 is-centered">
              <img id="recent-image" class="is-rounded" src="https://bulma.io/images/placeholders/128x128.png">
            </figure>
          </a>
        </div>
        <div class="column is-2">
          <a>
            <figure class="image is-128x128 is-centered">
              <img id="recent-image" class="is-rounded" src="https://bulma.io/images/placeholders/128x128.png">
            </figure>
          </a>
        </div>
        <div class="column is-2">
          <a>
            <figure class="image is-128x128 is-centered">
              <img id="recent-image" class="is-rounded" src="https://bulma.io/images/placeholders/128x128.png">
            </figure>
          </a>
        </div>
        <div class="column is-2">
          <a>
            <figure class="image is-128x128 is-centered">
              <img id="recent-image" class="is-rounded" src="https://bulma.io/images/placeholders/128x128.png">
            </figure>
          </a>
        </div>
        <div class="column is-2">
          <a>
            <figure class="image is-128x128 is-centered">
              <img id="recent-image" class="is-rounded" src="https://bulma.io/images/placeholders/128x128.png">
            </figure>
          </a>
        </div>
        <div class="column is-2">
          <a>
            <figure class="image is-128x128 is-centered">
              <img id="recent-image" class="is-rounded" src="https://bulma.io/images/placeholders/128x128.png">
            </figure>
          </a>
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
</style>