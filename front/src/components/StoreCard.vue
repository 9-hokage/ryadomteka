<template>
  <b-row class="my-5" align-v="center" align-h="between">
    <b-col cols="9">
      <h4  class="text-left font-weight-bold drug-name">
        {{store.name}}
      </h4>
      <div class="text-left text-muted">
        <div>
          {{store.address}}
        </div>
        <ul class="pl-3">
          <li class="dot">Открыто с 9:00 до 22:00</li>
        </ul>
      </div>
    </b-col>

    <b-col cols="3">
      <b-button size="lg" variant="primary" class="call-btn">
        <b-icon icon="telephone-fill" aria-label="Help"></b-icon>
      </b-button>
    </b-col>
    <hr>

  </b-row>

</template>

<script>
export default {
  name: "StoreCard",
  props: ['store']
}
</script>

<style scoped>

.drug-name {
  color: black !important;
}

.drug-name:hover {
  color: #505050 !important;
  cursor: pointer;
}
</style>
