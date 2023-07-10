# Write your MySQL query statement below
SELECT p.firstName,p.lastName,a.city,a.state 
FROM Person p
LEFT JOIN Address a 
ON p.personID = a.personID

#SELECT firstName, lastName, city, state FROM Person p LEFT JOIN Address a ON p.personId = a.personI