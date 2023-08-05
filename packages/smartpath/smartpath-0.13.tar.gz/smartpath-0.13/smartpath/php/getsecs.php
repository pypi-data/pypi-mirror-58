#!/usr/bin/php -q
<?php 

// confirm one parameter only  (usage: "test.php audiofilename.ogg")
if (count($argv) <> 2) {
  echo "-1\n";
  die(-1);
}
$fname = $argv[1];

// find and return number of seconds
require_once('getid3/getid3.php');
$getID3 = new getID3;
$id3info = $getID3->analyze($fname);
if (!array_key_exists('playtime_seconds', $id3info)) {
  echo "-2\n";
  die(-2);
}
$seconds = round($id3info['playtime_seconds'], 0);
echo $seconds."\n";
?>
