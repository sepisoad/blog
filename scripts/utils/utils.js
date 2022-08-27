import { ensureDirSync } from "https://deno.land/std/fs/mod.ts";
import { exec } from "https://deno.land/x/exec/mod.ts"
import { join } from "https://deno.land/std/path/mod.ts";


const pathJoin = (items) => {
  const newItems = items.filter(i => i !== null && i !== undefined) 
  const path = join(...newItems)
  return path
}

const forceCreateDir = (dirName) => {
  return ensureDirSync(dirName)
}

const listFilesInDir = (dirName) => {
  const allFiles = Array.from(Deno.readDirSync(dirName))
  const files = allFiles.filter(file => !file.name.startsWith("."))
  return files.map(f => f.name)
}

const runShellCommand = async (cmd) => {
  return await exec(cmd)
}

const moveFile = (from, to) => {
  return Deno.renameSync(from, to)
}

export {
  pathJoin,
  forceCreateDir,
  listFilesInDir,
  runShellCommand,
  moveFile
}