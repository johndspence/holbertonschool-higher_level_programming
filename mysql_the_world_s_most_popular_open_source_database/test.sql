show databases;

\!echo "\nTVShow";
select id,name,network_id from TVShow;
\!echo "\nSeason";
select * from Season;
\!echo "\nEpisode";
select id,name,number,season_id from Episode;
\!echo "\nTVShowGenre";
select * from TVShowGenre;
\!echo "\nGenre";
select * from Genre;
\!echo "\nNetwork";
select * from Network;
\!echo "\nTVShowActor";
select * from TVShowActor;
\!echo "\nActor";
select * from Actor;
