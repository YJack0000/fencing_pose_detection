<template>
  <container>
    <el-row>
      <el-col :span="24"><h1> Is this fencer? </h1></el-col>
    </el-row>
    <el-row>
      <el-col :span="24"><el-image style="width: 100px; height: 100px" src="https://fuss10.elemecdn.com/e/5d/4a731a90594a4af544c0c25941171jpeg.jpeg" fit="contain" /></el-col>
    </el-row>
    <el-row>
      <el-col :span="6" :offset="6"><el-button type="success" :icon="Check" circle /></el-col>
      <el-col :span="6"><el-button type="danger" :icon="Close" circle /></el-col>
    </el-row>
  </container>
</template>

<script setup>
import {
  Check as Check,
  Close as Close
} from '@element-plus/icons-vue'
</script>

<style scoped>
</style>
